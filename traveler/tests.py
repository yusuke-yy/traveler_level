from django.test import TestCase
from django.contrib.auth import get_user_model



class UserCreateTests(TestCase):

    def test_createuser(self):
        email = 'dummy@gmail.com'
        
        password = 'dummy'

        user = get_user_model().objects.create_user(email=email,password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))