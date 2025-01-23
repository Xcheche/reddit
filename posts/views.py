from django.shortcuts import render
from rest_framework import generics, permissions, serializers
from rest_framework.exceptions import ValidationError
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer

# Create your views here.

class  PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Make sure the user is authenticated before they can create a post
    
    # Make sure the user is authenticated before they can create a post
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
  
  
  
  
  
#Vote 

class VoteCreate(generics.CreateAPIView):
   
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated] # Make sure the user is authenticated before they can create a post
    
    # Make sure the user is authenticated before they can create a post
    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(id=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)
    
    # Creating a vote
    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise serializers.ValidationError("You have already voted for this post")
        serializer.save(poster=self.request.user, post=Post.objects.get(id=self.kwargs['pk']))