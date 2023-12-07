from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),
    path('', views.IndexView.as_view(), name='index'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('create', views.PostCreateView.as_view(), name='post_create'),
]