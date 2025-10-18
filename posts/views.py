from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Post
from .serializers import PostSerializer
from users.permissions import IsOwnerOrReadOnly 
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Get user_id from the URL
        user_id = self.kwargs['user_id']
        return Post.objects.filter(author__id=user_id)
    


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Get all users that the current user is following
        following_users = self.request.user.following.all()
        # Filter posts to only include those from the followed users
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    




    