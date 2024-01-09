from django.urls import path
from .views import article, index

urlpatterns = [
    path('', index, name='blog-index'),
    path('article-<str:numero_article>/', article, name='blog-article'),
]