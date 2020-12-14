from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('profile/<str:username>/', user_profile, name="user_profile"),
    path('profile/<str:username>/votes', votes, name="votes"),
    path('profile/<str:username>/submissions', submissions, name="submissions"),
    # Using Django defaults
    path('signup/', signup, name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='members/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
