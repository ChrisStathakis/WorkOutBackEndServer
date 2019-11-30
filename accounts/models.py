from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    birth  = models.DateField(blank=True, null=True)
