from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .serializers import UserSerializer

class CreateUserViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('register')
        self.user_data = {
            'username': 'testuser',
            'password': 'testpassword',
            'email': 'test@example.com'
        }

    def test_user_with_valid_data(self):
        response = self.client.post(self.register_url, data=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(username=self.user_data['username'])
        self.assertEqual(user.email, self.user_data['email'])
        serializer = UserSerializer(instance=user)
        self.assertEqual(response.data, serializer.data)

    def test_user_with_missing_data(self):
        invalid_data = {k:v for k,v in self.user_data.items() if k != 'email'}
        response = self.client.post(self.register_url, data=invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_with_existing_username(self):
        existing_user = User.objects.create_user(**self.user_data)
        response = self.client.post(self.register_url, data=self.user_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

