from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Note, Category
# from .forms import 

# Create your views here.
def index(request):
    """Index page for diary"""
    return render(request, 'diary/index.html')

def category_list(request):
    """Categories page that shows all categories"""
    category_list = Category.objects.all()
    return render(request, 'diary/category_list.html', {'categories': category_list})

def category(request, category_id):
    """Category page that shows one category and all of its notes"""
    category = Category.objects.get(id=category_id)
    notes = Note.objects.filter(category=category)
    return render(request, 'diary/category.html', {'category': category, 'notes': notes})

def all_notes(request):
    """ Listing all available notes on the /notes page """
    notes = Note.objects.order_by('date_added')
    # Dictionary containing all the notes. Keys - used in the template to access data. Values - data we send to the template.
    context = {'notes' : notes} 
    return render(request, 'diary/notes.html', context)
