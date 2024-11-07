from django import forms
from .models import Category, Note

#form for category creation
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name', 'category_colour']  # Include fields you want to display in the form

#form for note creation
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'my_note', 'importance', 'public']  # Include fields for the form

#form for editing notes + creating notes without a category
class NoteExtendedForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'my_note', 'importance', 'public', 'category']  # Include fields for the form