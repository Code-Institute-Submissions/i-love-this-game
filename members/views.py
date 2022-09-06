from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from .forms import ProfilePageForm
from theblog.models import Profile
from django.contrib.messages.views import SuccessMessageMixin


class CreateProfilePageView(SuccessMessageMixin, CreateView):
    """
    Django class-based view for create profile page
    """
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"
    success_message = "New user profile created"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(SuccessMessageMixin, generic.UpdateView):
    """
    Django class-based view for update profile page
    """
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = [
        'bio', 'profile_pic', 'website_url', 'youtube_url',
        'instagram_url', 'twitter_url', 'facebook_url'
    ]
    success_url = reverse_lazy('home')
    success_message = "User profile updated"


class ShowProfilePageView(DetailView):
    """
    Django class-based view for profile page
    """
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(
            *args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    """
    Django class-based view for update password page
    """
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')
    success_message = "Password updated"


def password_success(request):
    """
    Django function-based view for password success page
    """
    return render(request, 'registration/password_success.html', {})


class UserRegisterView(SuccessMessageMixin, generic.CreateView):
    """
    Django class-based view for register page
    """
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "Welcome! You are now a registered user - please log in"


class UserEditView(SuccessMessageMixin, generic.UpdateView):
    """
    Django class-based view for update settings page
    """
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    success_message = "User settings updated"

    def get_object(self):
        return self.request.user
