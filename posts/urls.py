from django.urls import path

from .views import PostList, VoteCreate

urlpatterns = [
    path("",PostList.as_view(), name="post-list"),
    path("<int:pk>/vote/", VoteCreate.as_view(), name="vote-create"),
    
]
