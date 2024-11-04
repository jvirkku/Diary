"""URL patterns for diary"""

from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    #Page that shows all created categories
    path('category_list/', views.category_list, name='category_list'),
    #Add category page
    path('add_category/', views.add_category, name='add_category'),
    #Page for a specific category and all its notes
    path('category/<int:category_id>/', views.category, name='category'),
    #Page for a specific note
    path('note/<int:note_id>/', views.note, name='note'),
    #Add note page
    path('category/<int:category_id>/add_note/', views.add_note, name='add_note'),
    #Add note page extended
    path('add_note_extended/', views.add_note_extended, name='add_note_extended'),
    #Edit note page
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    #Edit category page
    path('edit_category/<int:category_id>/', views.edit_category, name='edit_category'),
]