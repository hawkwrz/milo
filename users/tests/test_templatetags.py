import datetime

from django.test import SimpleTestCase

from users.templatetags.custom import age, bizzfuzz


class TestUrls(SimpleTestCase):

    def setUp(self):
        self.age1 = datetime.date(2000, 11, 1)
        self.age2 = datetime.now = datetime.date.today()
        self.number1 = 15
        self.number2 = 3
        self.number3 = 5
        self.number4 = 1

    def test_age(self):
        self.assertEqual("allowed", age(self.age1))

    def test_no_age(self):
        self.assertEqual("blocked", age(self.age2))

    def test_fizzbuzz(self):
        self.assertEqual("FizzBuzz", bizzfuzz(self.number1))

    def test_buzz(self):
        self.assertEqual("Fizz", bizzfuzz(self.number2))

    def test_fizz(self):
        self.assertEqual("Buzz", bizzfuzz(self.number3))

    def test_no_fizzbuzz(self):
        self.assertEqual(self.number4, bizzfuzz(self.number4))
