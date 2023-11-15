from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/', views.IndexView.as_view(), name='index'),
    path('blog/posts/', views.PostListView.as_view(), name='posts'),
]