from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('', views.UserListView.as_view(), name='list'),
    path('<int:pk>/', views.UserDetailView.as_view(), name='detail'),
    path('create', views.UserCreateView.as_view(), name='create'),
    path('<int:pk>/update', views.UserEditView.as_view(), name='edit'),
    path('<int:pk>/delete', views.UserDeleteView.as_view(), name='delete'),
]
