from django.urls import path
from blog.views import blog_posts, blog_posts_redirect

urlpatterns = [
    path('', blog_posts),
    path('list/', blog_posts, name='blog_posts'),
    path('redirect/', blog_posts_redirect),
]