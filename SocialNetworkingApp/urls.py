from django.urls import path
from . import views

urlpatterns = [
    # Define URL patterns for views within your app
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Add more URL patterns for other views as needed
]
