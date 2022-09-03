from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm, ProfilePageForm
from theblog.models import Profile
from django.contrib.messages.views import SuccessMessageMixin


# Django class-based view for create profile page
class CreateProfilePageView(SuccessMessageMixin, CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"
    # fields = '__all__'
    success_message = "New user profile created"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# Django class-based view for update profile page
class EditProfilePageView(SuccessMessageMixin, generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'youtube_url', 'instagram_url', 'twitter_url', 'facebook_url']
    success_url = reverse_lazy('home')
    success_message = "User profile updated"


# Django class-based view for profile page
class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(
            *args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


# Django class-based view for update password page
class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')
    # success_url = reverse_lazy('home')
    success_message = "Password updated"


# Django function-based view for password success page
def password_success(request):
    return render(request, 'registration/password_success.html', {})


# Django class-based view for register page
class UserRegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "Welcome! You are now a registered user - please log in"


# Django class-based view for update settings page
class UserEditView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    success_message = "User settings updated"

    def get_object(self):
        return self.request.user
