from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Create a new user with email is successful"""
        email = "almabud37@gmail.com"
        password = "test(12345678)"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        email = "test@ABAC.COM"
        user = get_user_model().objects.create_user(email, '12345678')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid(self):
        """Checking creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234567')

    def test_create_new_superuser(self):
        """Creating new super user with django custom User model"""
        user = get_user_model().objects.create_superuser(
            'almabud37@gmail.com',
            'test@1234567'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
