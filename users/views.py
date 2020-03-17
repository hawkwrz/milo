from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views import generic

from .forms import CreateUserForm

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
