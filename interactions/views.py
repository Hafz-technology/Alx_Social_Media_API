from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from users.models import CustomUser
from .models import Follow

from rest_framework import generics
from users.serializers import UserProfileSerializer 
# Create your views here.

class FollowToggleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        # The user to follow/unfollow
        user_to_toggle = CustomUser.objects.get(pk=user_id)
        # The user performing the action
        follower = request.user

        if follower == user_to_toggle:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        follow, created = Follow.objects.get_or_create(follower=follower, following=user_to_toggle)

        if created:
            # New follow
            return Response({"detail": f"You are now following {user_to_toggle.username}."}, status=status.HTTP_201_CREATED)
        else:
            # Unfollow
            follow.delete()
            return Response({"detail": f"You have unfollowed {user_to_toggle.username}."}, status=status.HTTP_204_NO_CONTENT)


class FollowingListView(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = CustomUser.objects.get(pk=user_id)
        return user.following.all()


class FollowersListView(generics.ListAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = CustomUser.objects.get(pk=user_id)
        return user.followers.all() 
    
    
