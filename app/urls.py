from django.urls import path
from django.contrib.auth.views import LogoutView
from app.views import IndexView, CustomLoginView, register, PostListView, PostDetailView, PostDeleteView, \
    PostCreateView, PostUpdateView, like_post, dislike_post, create_comment

urlpatterns = [
    path("", IndexView.as_view(), name="index"),  # Главная Страница
    path("auth/register", register, name="register"),  # Регистрация
    path("auth/login", CustomLoginView.as_view(), name="login"),  # Авторизация
    path("auth/logout", LogoutView.as_view(next_page="login"), name="logout"),  # Выход из учетки

    # Посты
    path("posts/", PostListView.as_view(), name="post-list"),  # Список постов
    path("posts/<int:pk>", PostDetailView.as_view(), name="post-detail"),  # Получение поста
    path("posts/delete/<int:pk>", PostDeleteView.as_view(), name="post-delete"),  # Удаление поста
    path("posts/create", PostCreateView.as_view(), name="post-create"),  # Создание поста
    path("posts/update/<int:pk>", PostUpdateView.as_view(), name="post-update"),  # Изменение поста

    # Лайк/дизлайк
    path("posts/<int:post_id>/like", like_post, name="like"),
    path("posts/<int:post_id>/dislike", dislike_post, name="dislike"),
    path("posts/<int:post_id>/comment", create_comment, name="comment"),
]
