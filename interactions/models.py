from django.db import models
from django.conf import settings

# Create your models here.

class Follow(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following_relations', on_delete=models.CASCADE)
    following = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='follower_relations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # To ensures that the user can't follow the same person more than once
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower.username} follows {self.following.username}'
    
    
    