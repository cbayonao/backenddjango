"""
Model for posts
"""
# Django imports
from django.db import models


class User(models.Model):
    """
    Define the user class
    """
    email = models.EmailField(unique=True)
    passwd = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    country = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    bio = models.TextField(blank=True)
    birthDate = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Para hacer la representación en string de un objeto
    def __str__(self):
        """
        Metodo para representar en string de los objetos
        """
        return self.email