from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test to create user with email successful"""
        email = 'testone1@gmail.com'
        password = 'test1one'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalize(self):
        """Test for email new user is normalized"""
        email = 'testtwo2@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'test2two')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no or invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test3three')

    def test_create_new_superuser(self):
        """Test creating a new Super User"""
        user = get_user_model().objects.create_superuser(
            'testfour4@gmail.com',
            'test4four'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

        