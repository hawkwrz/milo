import datetime

from django.test import TestCase, Client
from django.urls import reverse

from users.models import CustomUser


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create(
            username="TestCaseUser",
            password="Test!2#4",
            birthday=datetime.date.today(),
        )
        self.list_url = reverse('users:list')
        self.detail_url = reverse('users:detail', args=[self.user.pk])
        self.delete_url = reverse('users:delete', args=[self.user.pk])

    def test_user_list(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/customuser_list.html')

    def test_user_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/customuser_detail.html')

    def test_user_create_POST(self):
        url = reverse('users:create')
        data = {
            'username': 'TestCaseUser123',
            'password': "Test!2#4",
            'password1': "Test!2#4",
            'password2': "Test!2#4",
            'birthday': datetime.date.today()
        }
        response = self.client.post(url, data)

        test_user = CustomUser.objects.all().filter(username="TestCaseUser123").get()
        success_url = reverse('users:detail', args=[test_user.pk, ])

        self.assertEquals(test_user.username, 'TestCaseUser123')
        self.assertRedirects(response, success_url)

    def test_delete_post_request(self):
        post_response = self.client.post(reverse('users:delete', args=(self.user.pk,)), follow=True)
        self.assertRedirects(post_response, reverse('users:list'), status_code=302)

    def test_user_edit(self):
        url = reverse('users:edit', args=[self.user.pk])
        data = {
            'username': 'TestCaseUserChange',
            'password1': "Test!2#4",
            'password2': "Test!2#4",
            'birthday': datetime.date.today()
        }
        response = self.client.post(url, data)

        test_user = CustomUser.objects.all().filter(username="TestCaseUserChange").get()
        success_url = reverse('users:detail', args=[test_user.pk])
        self.assertEquals(test_user.username, 'TestCaseUserChange')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, success_url)
