from django.contrib import admin
from dejavu.models import Reservation
from dejavu.models import Session
from dejavu.models import Hour
from dejavu.models import Day
from dejavu.models import SessionTemplate
from dejavu.models import Subscriber


class HourAdmin(admin.ModelAdmin):
    list_display = ('hour_range',)
    search_fields = ['hour']
    ordering = ['hour']


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user_info', 'session', 'assisted')
    list_editable = ('assisted',)
    search_fields = [
        'user__first_name', 'user__last_name', 'user__username']
    ordering = ['user', 'assisted']
    list_per_page = 20


class ReservationAdminInline(admin.TabularInline):
    model = Reservation


class SessionAdmin(admin.ModelAdmin):
    inlines = (ReservationAdminInline,)
    list_display = ('date', 'hour')
    search_fields = [
        'date', 'hour__hour']
    ordering = ['date', 'hour__hour']
    list_per_page = 20


class DayAdmin(admin.ModelAdmin):
    list_display = ('name', 'weekday')
    search_fields = ['name', 'weekday']
    ordering = ['weekday']


class SessionTemplateAdmin(admin.ModelAdmin):
    list_display = ('day', 'hour')
    search_fields = ['day__name', 'hour__hour']
    ordering = ['day', 'hour__hour']


class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'wods',
    )
    search_fields = [
        'user__first_name', 'user__last_name', 'user__username', 'wods'
    ]
    ordering = ['user', 'wods']


admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Hour, HourAdmin)
admin.site.register(Day, DayAdmin)
admin.site.register(SessionTemplate, SessionTemplateAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
