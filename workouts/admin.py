from django.contrib import admin

from .models import WorkOut, WorkOutParts


class WorkOutPartsInline(admin.TabularInline):
    model = WorkOutParts


@admin.register(WorkOut)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'user_related', 'public', 'status']
    list_filter = ['public', 'status', 'category' ]
    search_fields = ['title']
    inlines = [WorkOutPartsInline, ]


@admin.register(WorkOutParts)
class WorkoutPartsAdmin(admin.ModelAdmin):
    list_display = ['exercise_related', 'workout_related']
    list_filter = ['exercise_related', 'workout_related']
