from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'test@gmail.com'
        password = '113776'
        user = get_user_model()(email=email, password=password)
        user.save()
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        email = 'test@GMAIL.COM'
        user = get_user_model()(email=email, password='113777')
        user.save()
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model()(None, '134567').save()
