from django.urls import path
from . import views

app_name = 'blog'  # дублируется в include, но оставим
urlpatterns = [
    path('', views.index, name='index'),  # адрес: ''
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts, name='category_posts'),
]
