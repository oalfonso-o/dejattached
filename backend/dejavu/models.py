from datetime import time, datetime

from django.db import models
from django.db import IntegrityError
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.html import format_html
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Hour(models.Model):
    class Meta:
        verbose_name = 'Hora'

    hour = models.TimeField('Hora de la sessión', unique=True)

    def __str__(self):
        return self.hour_range()

    def hour_range(self):
        return '{} - {}'.format(
            self.hour.isoformat()[:5],
            time(
                hour=self.hour.hour + 1,
                minute=self.hour.minute).isoformat()[:5]
            )
    hour_range.short_description = 'Rango de horas'

    def hour_simple(self):
        return self.hour.isoformat()[:5]
    hour_simple.short_description = 'Hora'


class Reservation(models.Model):
    class Meta:
        verbose_name = 'Reserva'
        unique_together = ('user', 'session')

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    session = models.ForeignKey(
        'Session', on_delete=models.CASCADE, null=False)
    assisted = models.BooleanField('Asistencia', default=True)

    def user_info(self):
        return format_html(
            '<span style="color: green;">{}: </span>{} {}',
            self.user.username,
            self.user.first_name,
            self.user.last_name,
        )

    def __str__(self):
        return ('{} {}'.format(self.user.first_name, self.user.last_name) if
                self.user.first_name else self.user.username)

    def save(self, *args, **kwargs):
        if self.session.reservation_set.count() < 10:
            super(Reservation, self).save(*args, **kwargs)
        else:
            raise IntegrityError


class Session(models.Model):
    class Meta:
        verbose_name = 'Sesión'
        verbose_name_plural = 'Sesiones'
        unique_together = ('date', 'hour')

    date = models.DateField('Día', default=True)
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return '{} - {}'.format(self.date, self.hour.hour_simple())

    def datetime(self):
        return datetime.combine(self.date, self.hour.hour)

    def is_closed(self):
        return bool(self.datetime() < datetime.now())


class Day(models.Model):
    class Meta:
        verbose_name = 'Día'

    def __str__(self):
        return self.name

    name = models.CharField('Día de la semana', max_length=20, unique=True)
    weekday = models.IntegerField(
        'Número de dia de la semana (Lunes es 0)', unique=True)


class SessionTemplate(models.Model):
    class Meta:
        verbose_name = 'Plantilla de Sesión'
        verbose_name_plural = 'Plantillas de Sesión'
        unique_together = ('day', 'hour')

    day = models.ForeignKey(Day, on_delete=models.CASCADE, null=False)
    hour = models.ForeignKey(Hour, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return '{} - {}'.format(self.day, self.hour.hour_simple())


class Subscriber(models.Model):
    class Meta:
        verbose_name = 'Abonado'

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='subscriber')
    wods = models.IntegerField(default=0)

    def __str__(self):
        return '#{} - {}'.format(self.id, self.user)

    def username(self):
        return self.user.username

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name


@receiver(models.signals.post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        Subscriber.objects.create(user=instance, wods=1)
