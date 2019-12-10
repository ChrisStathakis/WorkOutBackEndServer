from django.db import models

from exercises.models import Exercise
from accounts.models import User


class WorkOut(models.Model):
    CHOICES = (
        ('a', 'AMRAP'),
        ('b', 'Rounds'),
        ('c', 'For Time'),
        ('d', 'Tabata'),
    )
    status = models.BooleanField(default=True)
    public = models.BooleanField(default=True)
    title = models.CharField(max_length=220)
    category = models.CharField(max_length=1, choices=CHOICES, default='a')
    duration = models.PositiveIntegerField(default=0)
    rounds = models.PositiveIntegerField(default=0)
    guide = models.TextField(blank=True)
    user_related = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def tag_user(self):
        return self.user_related.username

    def tag_category(self):
        return self.get_category_display()


class WorkOutParts(models.Model):
    exercise_related = models.ForeignKey(Exercise, on_delete=models.PROTECT)
    title = models.CharField(max_length=220)
    guide = models.TextField(blank=True)
    workout_related = models.ForeignKey(WorkOut, on_delete=models.CASCADE)

    def __str__(self):
        return self.title