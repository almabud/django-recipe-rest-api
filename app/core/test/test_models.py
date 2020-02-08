from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_new_user_with_email_successful(self):
        """Create new user with email"""

        email = "almabud37@gmail.com"
        password = "bd464258"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_new_user_email_normalize(self):
        """Check email is normalize or not"""
        email = "almabud37@Gmail.com"
        password = "bd464258"
        user = get_user_model().objects.create_user(email, password)
        self.assertEqual(user.email, email.lower())

