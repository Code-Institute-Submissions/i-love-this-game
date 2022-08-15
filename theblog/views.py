from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# def home(request):
#     return render(request, 'home.html', {})


# Django class-based view for the Home page
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    paginate_by = 8


# Django class-based view for post page
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
