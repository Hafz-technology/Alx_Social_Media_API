from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class CustomUser(AbstractUser):
    
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, max_length=500)
    following = models.ManyToManyField('self',through='interactions.Follow',
                                        related_name='followers',symmetrical=False
                )

    def __str__(self):
        return self.username
    


