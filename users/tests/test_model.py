import datetime

from django.test import TestCase

from users.models import CustomUser


class TestModels(TestCase):
    def setUp(self):
        self.time = datetime.date.today()
        self.user = CustomUser.objects.create(
            username="TestCaseUser",
            password="Test!2#4",
            birthday=self.time,
        )

    def test_user_number(self):
        self.assertIsNotNone(self.user.number)

    def test_birthday(self):
        self.assertEqual(self.user.birthday, self.time)
