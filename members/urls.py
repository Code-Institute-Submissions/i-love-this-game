from django.urls import path
from .views import UserRegisterView


# URLs for each HTML view in the members app
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
]
