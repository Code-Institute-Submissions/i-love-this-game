from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


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


# Django class-based view for add post page
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')
