from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

# Create your tests here.


class UserRegistrationTest(APITestCase):
    def test_registration(self):
        url = reverse('auth_register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'somepassword',
            'password2': 'somepassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
        
        
