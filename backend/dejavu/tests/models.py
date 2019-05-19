from django.test import TestCase
from dejavu.models import Day


class ModelTestCase(TestCase):

    def setUp(self):
        self.day = Day(
            name='Friday',
            weekday=4,
        )

    def test_model_can_create_a_day(self):
        old_count = Day.objects.count()
        self.day.save()
        new_count = Day.objects.count()
        self.assertNotEqual(old_count, new_count)
