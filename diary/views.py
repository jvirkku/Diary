from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Note, Category
from .forms import CategoryForm, NoteForm, NoteExtendedForm
from django.db.models import Q

# Create your views here.
def index(request):
    """Index page for diary"""
    if request.user.is_authenticated:
         notes= Note.objects.filter(Q(owner=request.user) | Q(public=True)).order_by('date_added')
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
    #notes = Note.objects.filter(category=category)
    notes= Note.objects.filter(category=category).order_by('date_added')
    notes= Note.objects.filter(Q(owner=request.user, category=category) | Q(public=True, category=category)).order_by('date_added')
    #if note.owner != request.user:
    #    raise Http404
    return render(request, 'diary/category.html', {'category': category, 'notes': notes})

@login_required
def edit_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('diary:category', category_id=category.id)
    else:
        form = CategoryForm(instance=category)

    return render(request, 'diary/edit_category.html', {'form': form, 'category': category})

@login_required
def add_note(request, category_id):
    """Add note page"""
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            #note = form.save(commit=False)
            #note.category = category
            #note.save()
            note = form.save(commit=False)
            note.category = category
            note.owner=request.user
            note.save()

            return redirect('diary:category', category_id=category.id)
    else:
        form = NoteForm()
    
    return render(request, 'diary/add_note.html', {'form': form, 'category': category})

@login_required
#This is for the Index page "add note" button 
def add_note_extended(request):
    categories = Category.objects.all()  # Get all categories
    form = NoteExtendedForm(request.POST or None)
    
    if request.method == "POST" and form.is_valid():
        note = form.save(commit=False)
        # Get the selected category by its ID
        category_id = request.POST.get('category')
        note.category = Category.objects.get(id=category_id)
        note.owner=request.user
        note.save()
        return redirect('diary:index')  # Redirect after saving
    
    return render(request, 'diary/add_note_extended.html', {'form': form, 'categories': categories})

@login_required
def note(request, note_id):
    """Note page that shows the contents of a single note"""
    note = Note.objects.get(id=note_id)
    return render(request, 'diary/note.html', {'note': note})

@login_required
def edit_note(request, note_id):
    note = Note.objects.get(id=note_id)
    if note.owner != request.user:
        raise Http404
    if request.method == 'POST':
        form = NoteExtendedForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('diary:note', note_id=note.id)
    else:
        form = NoteExtendedForm(instance=note)

    return render(request, 'diary/edit_note.html', {'form': form, 'note': note})