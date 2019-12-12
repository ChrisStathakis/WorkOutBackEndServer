from rest_framework import serializers

from ..models import Planner, PlannerWorkOut


class PlannerSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='planner:detail', read_only=True)

    class Meta:
        model = Planner
        fields = ['title', 'id', 'active', 'user', 'guide', 'url']


class PlannerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planner
        fields = ['title', 'id', 'guide', 'planner_workouts', 'user']


class PlannerWorkoutSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='planner:workout_detail', read_only=True)

    class Meta:
        model = PlannerWorkOut
        fields = ['workout', 'planner_related', 'tag_workout', 'tag_planner_related',
                  'is_done', 'id'
                  ]


class PlannerWorkoutDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlannerWorkOut
        fields = ['workout', 'planner_related', 'tag_workout', 'tag_planner_related',
                  'is_done', 'exercises', 'id'
                  ]
