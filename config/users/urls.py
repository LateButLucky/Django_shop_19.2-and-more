from django.urls import path
from .views import SignUpView, ProfileView, CustomPasswordResetView

app_name = 'users'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]
