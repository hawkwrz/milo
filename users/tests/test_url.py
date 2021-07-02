from django.test import SimpleTestCase
from django.urls import reverse, resolve

from users.views import UserListView, UserDetailView, UserCreateView, UserEditView


class TestUrls(SimpleTestCase):

    def test_list_url_resolves(self):
        url = reverse('users:list')
        self.assertEquals(resolve(url).func.view_class, UserListView)

    def test_detail_url_resolves(self):
        url = reverse('users:detail', args=['1'])
        self.assertEquals(resolve(url).func.view_class, UserDetailView)

    def test_create_url_resolves(self):
        url = reverse('users:create')
        self.assertEquals(resolve(url).func.view_class, UserCreateView)

    def test_edit_url_resolves(self):
        url = reverse('users:edit', args=['1'])
        self.assertEquals(resolve(url).func.view_class, UserEditView)
