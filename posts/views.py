from django.shortcuts import render
from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer

# Create your views here.

class  PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Make sure the user is authenticated before they can create a post
    
    # Make sure the user is authenticated before they can create a post
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
  