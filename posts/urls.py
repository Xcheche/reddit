from django.urls import path
from .import views

urlpatterns = [
    path('PostList/', views.PostList.as_view(), name='PostList')
]