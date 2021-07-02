import datetime

from django.test import TestCase

from users.forms import CreateUserForm


class TestForms(TestCase):

    def test_create_user_valid_data(self):
        form = CreateUserForm(data={
            'username': 'TestUserCase',
            'birthday': datetime.datetime.today(),
            'password1': 'Test!2#4',
            'password2': 'Test!2#4',
        })

        self.assertTrue(form.is_valid())

    def test_create_user_no_data(self):
        form = CreateUserForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
