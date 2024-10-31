from django.shortcuts import render

# Create your views here.
def index(request):
    """Index page for diary"""
    return render(request, 'diary/index.html')
