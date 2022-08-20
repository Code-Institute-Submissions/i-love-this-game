from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


# def home(request):
#     return render(request, 'home.html', {})


# Django class-based view for the Home page
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    # ordering = ['-id']
    paginate_by = 5


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


# Django class-based view for add category page
class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title', 'body')


# Django class-based view for update post page
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']


# Django class-based view for delete post page
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
