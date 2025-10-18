from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserPostsView, FeedView 

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

urlpatterns = [
    path('feed/', FeedView.as_view(), name='user-feed'),
    path('user/<int:user_id>/', UserPostsView.as_view(), name='user-posts-list'),
    path('', include(router.urls)),
]




