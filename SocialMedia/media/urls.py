from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name='register'),
    path("login", views.login_user, name='login' ),
    path("logoug", views.logout_user, name='logout'),
    path("newpost", views.new_posts, name='newposts'),

    # Api requests
    path("post_api", views.post_api, name='post_api'),
    path("get_api", views.get_api, name='getapi')
    
]