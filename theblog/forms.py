from django import forms
from .models import Post, Comment, Contact


class PostForm(forms.ModelForm):
    """
    Class to create form fields for the add post page
    """
    class Meta:
        model = Post
        fields = (
            'title', 'title_tag', 'author',
            'category', 'body', 'snippet', 'header_image'
            )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={
                'class': 'form-control', 'value': '',
                'id': 'user', 'type': 'hidden'
                }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    """
    Class to create form fields for the update post page
    """
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    """
    Class to create form fields for the create comment page
    """
    class Meta:
        model = Comment
        fields = ('body',)

        widgets = {

            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ContactCreateForm(forms.ModelForm):
    """
    Class to create form fields for the update post page
    """
    class Meta:
        model = Contact
        fields = ('author', 'subject', 'body')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
