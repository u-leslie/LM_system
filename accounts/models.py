from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    email = models.EmailField(unique=True)
    is_driver = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_userprofile_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_userprofile_set',  # Avoid clashes with auth.User.user_permissions
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username
