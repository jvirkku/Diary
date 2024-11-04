from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Note, Category
from .forms import CategoryForm, NoteForm

# Create your views here.
def index(request):
    """Index page for diary"""
    if request.user.is_authenticated:
         notes = Note.objects.order_by('date_added')
         context = {'notes' : notes} 
    else:
        notes = Note.objects.filter(public=True).order_by('date_added') #if not logged in, public notes are visible
        # Dictionary containing all the notes. Keys - used in the template to access data. Values - data we send to the template.
        context = {'notes' : notes} 
    return render(request, 'diary/index.html', context)



@login_required
def category_list(request):
    """Categories page that shows all categories"""
    category_list = Category.objects.all()
    return render(request, 'diary/category_list.html', {'categories': category_list})

@login_required
def add_category(request):
    """Add category page"""
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diary:category_list')  # Redirect to the category list page after saving
    else:
        form = CategoryForm()
    
    return render(request, 'diary/add_category.html', {'form': form})

@login_required
def category(request, category_id):
    """Category page that shows one category and all of its notes"""
    category = Category.objects.get(id=category_id)
    notes = Note.objects.filter(category=category)
    return render(request, 'diary/category.html', {'category': category, 'notes': notes})

@login_required
def add_note(request, category_id):
    """Add note page"""
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.category = category
            note.save()
            return redirect('diary:category', category_id=category.id)
    else:
        form = NoteForm()
    
    return render(request, 'diary/add_note.html', {'form': form, 'category': category})


@login_required
def note(request, note_id):
    """Note page that shows the contents of a single note"""
    note = Note.objects.get(id=note_id)
    return render(request, 'diary/note.html', {'note': note})