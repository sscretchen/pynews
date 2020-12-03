from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name="index"),
    path('about/', about, name="about"),
    # Need unique ID for each post later ex: <int:pk>
    path('post_detail/', post_detail, name="post_detail"),
]
