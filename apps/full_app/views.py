from django.shortcuts import render, redirect
from .models import Books

def index(request):
    context = {
    'books' : Books.objects.all()
    }
    return render(request, "courses_app/index.html", context)

def submit(request):
    Books.objects.create(title=request.POST['title'],author=request.POST['author'],category=request.POST['category'])
    return redirect('/')
# Create your views here.
