"""
Posts models
"""
# django imports
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    """
    post model
    """
    # On delete cada vez q se borre un user se borran todos sus posts
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        """
        Retorna el username del user
        """
        return f'{self.title} by @{self.user.username}'