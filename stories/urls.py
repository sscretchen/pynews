from django.urls import path
from .views import *


urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('submit_story/', submit_story, name="submit_story"),
]
