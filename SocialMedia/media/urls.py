from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name='register'),
    path("login", views.login_user, name='login' ),
    path("logout", views.logout_user, name='logout'),
    path("newpost", views.new_posts, name='newposts'),
    path("profile/<int:user_id>", views.user_profile, name='profile'),

    # Api requests
    path("post_api", views.post_api, name='post_api'),
    path("get_api", views.get_api, name='getapi')
    
]