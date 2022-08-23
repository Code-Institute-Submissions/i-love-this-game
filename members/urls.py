from django.urls import path
from .views import UserRegisterView, UserEditView


# URLs for each HTML view in the members app
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]
