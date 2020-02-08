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

    def test_user_invalid_email(self):
        """Test creating user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "bd464258")

    def test_create_super_user(self):
        """Test creation of super user"""
        email = "almabud37@gmail.com"
        password = "bd464258"
        user = get_user_model().objects.create_superuser(email, password)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
