from django.db import models
from tinymce.models import HTMLField


class ExerciseCategory(models.Model):
    title = models.CharField(unique=True, max_length=240)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Exercise(models.Model):
    status = models.BooleanField(default=True)
    title = models.CharField(unique=True, max_length=200)
    category = models.ForeignKey(ExerciseCategory, null=True, on_delete=models.CASCADE)
    url = models.URLField(blank=True)
    guide = HTMLField()

    def __str__(self):
        return self.title

    def tag_category(self):
        return self.category.title