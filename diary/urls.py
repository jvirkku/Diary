"""URL patterns for diary"""

from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    # Listing all notes
    path('notes/', views.all_notes, name='all_notes')
]