from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('addPost/', views.AddPost.as_view(), name='addPost'),
    path('<slug:slug>/', views.PostDetail.as_view(),  name='post_detail'),
]