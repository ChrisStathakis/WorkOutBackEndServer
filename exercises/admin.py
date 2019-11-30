from django.contrib import admin

from .models import Exercise, ExerciseCategory


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_filter = ['status']
    search_fields = ['title']
    list_select_related = ['category']


@admin.register(ExerciseCategory)
class ExerciseCategoryAdmin(admin.ModelAdmin):
    pass


