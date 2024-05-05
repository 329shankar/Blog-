from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'base.html')

def show_posts(request):
    # Fetch all posts from the database
    posts = Post.objects.all()

    # Pass the posts queryset to the template
    print(posts)
    return render(request, 'posts.html', {'posts': posts})

def about(request):
     return render(request,'about.html')

def Homepage(request):
    return render(request,'Homepage.html')


