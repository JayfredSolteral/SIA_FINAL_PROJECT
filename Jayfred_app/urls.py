from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Home, AddItem, landing, register, EditItem, DeleteItem


urlpatterns = [
    path('', landing, name='landing'),
    path('items/', Home, name='home'),
    path('add-item/', AddItem, name='add_item'),
    path('edit-item/<int:pk>/', EditItem, name='edit_item'),
    path('delete-item/<int:pk>/', DeleteItem, name='delete_item'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]