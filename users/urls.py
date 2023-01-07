from django.urls import path

from .views import RegisterView, LoginView, ProfileView, LogoutView, ProfileUpdateView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile-edit'),
    path('profile/', ProfileView.as_view(), name='profile'),
]