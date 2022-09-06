from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic import DeleteView
from django.http import HttpResponseRedirect
from .models import Post, Category, Comment, Contact
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.messages.views import SuccessMessageMixin


# Django function-based view for the like button
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    # liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        # liked = False
    else:
        post.likes.add(request.user)
        # liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


# Django class-based view for the home page
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


# Django function-based view for the category list page
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(
        request, 'category_list.html', {'cat_menu_list': cat_menu_list})


# Django function-based view for the categories page
def CategoryView(request, cats):
    category_posts = Post.objects.filter(
        category__name__iexact=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title(
    ).replace('-', ' '), 'category_posts': category_posts})


# Django class-based view for the post page
class ArticleDetailView(DetailView):
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


# Django class-based view for the create post page
class AddPostView(SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = '/'
    success_message = "Article created"


# Django class-based view for the create comment page
class AddCommentView(SuccessMessageMixin, CreateView):
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


# Django class-based view for the create category page
class AddCategoryView(SuccessMessageMixin, CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    success_message = "Category created"


# Django class-based view for the update post page
class UpdatePostView(SuccessMessageMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_message = "Article updated"

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.object.pk})


# Django class-based view for the delete post page
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


# Django class-based view for the contact page
class ContactCreateView(SuccessMessageMixin, CreateView):
    model = Contact
    template_name = 'contact.html'
    fields = ['subject', 'body']
    success_url = reverse_lazy('home')
    success_message = "Message sent"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Django function-based view for the about page
def AboutView(request):
    return render(request, 'about.html')
