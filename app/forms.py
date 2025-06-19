# forms

from django import forms
from django.contrib.auth.models import User

from app.models import Post, Comment, Report, Media
from django.contrib.auth.forms import UserCreationForm, UserChangeForm as BaseUserChangeForm


class PostMediaForm(forms.ModelForm):
    url = forms.URLField(required=False)
    file = forms.ImageField(required=False)

    class Meta:
        model = Media
        fields = ["url", "file"]

    # Проверка на то что пользователь дал ссылку или изображение
    def clean(self):
        cleaned_data = super().clean()
        url = cleaned_data.get("url")
        file = cleaned_data.get("file")

        if url and file:
            raise forms.ValidationError("Нельзя указывать и ссылку и файл одновременно")
        if not url and not file:
            raise forms.ValidationError("Нужно указать либо ссылку либо файл")
        return cleaned_data


MediaFormSet = forms.inlineformset_factory(
    Post, Media,
    form=PostMediaForm,
    extra=3,
    can_delete=True
)


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


class ReportForm(forms.ModelForm):
    description = forms.CharField(max_length=1024, widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "rows": 3,
            "placeholder": "Опишите причину жалобы..."
        }
    ))

    class Meta:
        fields = ["theme", "description"]
        model = Report
        widgets = {
            "theme": forms.Select(
                attrs={
                    "class": "form-select"
                }
            )
        }


class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email"
        )
