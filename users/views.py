import csv

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .forms import CreateUserForm
from .templatetags.custom import bizzfuzz, age

User = get_user_model()


class UserListView(generic.ListView):
    model = User


class UserDetailView(generic.DetailView):
    model = User
    context_object_name = 'user'
    queryset = User.objects.all()


class UserCreateView(generic.CreateView):
    model = User
    form_class = CreateUserForm

    def get_success_url(self):
        return reverse('users:detail', args=(self.object.id,))


class UserEditView(generic.UpdateView):
    model = User
    template_name_suffix = '_update_form'
    form_class = CreateUserForm

    def get_success_url(self):
        return reverse('users:detail', args=(self.object.id,))


class UserDeleteView(generic.DeleteView):
    model = User
    context_object_name = 'user'

    def get_success_url(self):
        return reverse('users:list')


class HomeView(generic.RedirectView):
    pattern_name = 'users:list'


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="UserList.csv"'
    users = User.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])
    for user in users:
        writer.writerow([user.username, user.birthday.strftime("%d/%m/%Y"),
                         age(user.birthday), user.number, bizzfuzz(user.number)])
    return response
