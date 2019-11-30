from rest_framework import serializers

from ..models import ExerciseCategory, Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='exercise:detail_view', read_only=True)

    class Meta:
        model = Exercise
        fields = ['title', 'id', 'category', 'tag_category', 'detail']


class ExerciseRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ['id', 'status', 'title', 'url', 'guide', 'category', 'tag_category']


class ExerciseCategorySerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='exercise:category_detail', read_only=True)

    class Meta:
        model = ExerciseCategory
        fields = '__all__'


