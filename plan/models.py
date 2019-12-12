from django.db import models

from accounts.models import User
from workouts.models import WorkOut


class Planner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
    title = models.CharField(max_length=220)
    guide = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def planner_workouts(self):
        return self.plans.all().values('id', 'workout__title', 'workout')


class PlannerWorkOut(models.Model):
    planner_related = models.ForeignKey(Planner, on_delete=models.CASCADE, related_name='plans')
    workout = models.ForeignKey(WorkOut, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    date_done = models.DateField(blank=True, null=True)
    title = models.CharField(blank=True, max_length=200)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.workout.title

    def tag_workout(self):
        return self.workout.title

    def tag_planner_related(self):
        return self.planner_related.title

    def exercises(self):
        return self.workout.workoutparts_set.values('id', 'exercise_related__title')
