from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView, PasswordChangeView
from app.views import IndexView, CustomLoginView, register, PostListView, PostDetailView, PostDeleteView, \
    PostCreateView, PostUpdateView, like_post, dislike_post, create_comment, create_report, RepostListView, \
    UserUpdateView, UserPostListView, profile_view

urlpatterns = [
    path("", IndexView.as_view(), name="index"),  # Главная Страница
    path("auth/register", register, name="register"),  # Регистрация
    path("auth/login", CustomLoginView.as_view(), name="login"),  # Авторизация
    path("auth/logout", LogoutView.as_view(next_page="login"), name="logout"),  # Выход из учетки
    # Изменение пароля
    path("auth/change-password", PasswordChangeView.as_view(
        template_name="app/change_password.html", success_url=reverse_lazy("index")
    ), name="password-change"),
    # Изменение информации пользователя
    path("accounts/profile/", profile_view, name="profile"),
    path("accounts/profile/update/<int:pk>", UserUpdateView.as_view(), name="user-update"),
    path("accounts/profile/posts", UserPostListView.as_view(), name="user-posts"),

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

    # Жалобы
    path("posts/<int:post_id>/report", create_report, name="create-report"),
    path("reports/", RepostListView.as_view(), name="report-list"),
]
