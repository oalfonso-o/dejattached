from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework import status

from dejavu.views import DayApiView


class ViewTestCase(TestCase):

    def setUp(self):
        factory = APIRequestFactory()
        request = factory.get(reverse('days'), format='json')
        user = User(username='test')
        user.save()
        force_authenticate(request, user=user, token=user.auth_token)
        view = DayApiView.as_view()
        self.response = view(request)

    def test_api_can_get_days(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
