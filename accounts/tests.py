from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class AccountsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

    def test_register_view(self):
        response = self.client.post(reverse('register'), {
            "username": "newuser",
            "password1": "StrongPass123!",
            "password2": "StrongPass123!",
        })
        self.assertEqual(response.status_code, 302)  # redirects on success
        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_login_view(self):
        response = self.client.post(reverse('login'), {
            "username": "testuser",
            "password": "testpass",
        })
        self.assertEqual(response.status_code, 302)  # redirect after login

    def test_profile_view_requires_login(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)  # redirect to login page
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)  # works if logged in

# Create your tests here.
