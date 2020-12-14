from django.urls import path
from .views import *


urlpatterns = [
    path('', frontpage, name="frontpage"),
    path('search/', search, name="search"),
    path('submit_story/', submit_story, name="submit_story"),
    path('story/<int:story_id>/vote/', vote, name="vote"),
    path('story/<int:story_id>/', story_detail, name="story_detail"),
]
