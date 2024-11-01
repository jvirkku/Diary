"""URL patterns for diary"""

from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    #Page that shows all created categories
    path('category_list/', views.category_list, name='category_list'),
    #Page for a specific category and all its notes
    path('category/<int:category_id>/', views.category, name='category'),
    # Listing all notes
    path('notes/', views.all_notes, name='all_notes'),
]