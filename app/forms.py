# forms

from django import forms
from django.contrib.auth.models import User

from app.models import Post, Comment
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):
    """
    Форма Поста, нужна для Создания либо Изменения Поста
    """
    title = forms.CharField(max_length=255)
    content = forms.CharField(max_length=3000)

    class Meta:
        model = Post
        fields = ["title", "content"]


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": "3",
        "placeholder": "Напишите комментарий...",
    }))

    class Meta:
        model = Comment
        fields = ["body"]
