from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect
from .models import Post, Category, Comment, Contact
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin


def LikeView(request, pk):
    """
    Django function-based view for the like button
    """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    """
    Django class-based view for the home page
    """
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryListView(request):
    """
    Django function-based view for the category list page
    """
    cat_menu_list = Category.objects.all()
    return render(
        request, 'category_list.html', {'cat_menu_list': cat_menu_list})


def CategoryView(request, cats):
    """
    Django function-based view for the categories page
    """
    category_posts = Post.objects.filter(
        category__name__iexact=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title(
    ).replace('-', ' '), 'category_posts': category_posts})


class ArticleDetailView(DetailView):
    """
    Django class-based view for the post page
    """
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes()
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(SuccessMessageMixin, CreateView):
    """
    Django class-based view for the create post page
    """
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = '/'
    success_message = "Article created"


class AddCommentView(SuccessMessageMixin, CreateView):
    """
    Django class-based view for the create comment page
    """
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_message = "Comment created"

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.object.post_id})


class AddCategoryView(SuccessMessageMixin, CreateView):
    """
    Django class-based view for the create category page
    """
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    success_message = "Category created"


class UpdatePostView(SuccessMessageMixin, UpdateView):
    """
    Django class-based view for the update post page
    """
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_message = "Article updated"

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.object.pk})


class DeletePostView(DeleteView):
    """
    Django class-based view for the delete post page
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class ContactCreateView(SuccessMessageMixin, CreateView):
    """
    Django class-based view for the contact page
    """
    model = Contact
    template_name = 'contact.html'
    fields = ['subject', 'body']
    success_url = reverse_lazy('home')
    success_message = "Message sent"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def AboutView(request):
    """
    Django function-based view for the about page
    """
    return render(request, 'about.html')
