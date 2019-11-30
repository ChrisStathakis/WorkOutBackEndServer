from rest_framework import serializers
from ..models import WorkOut, WorkOutParts, User


class WorkOutSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='workout:detail', read_only=True)

    class Meta:
        model = WorkOut
        fields = ['status', 'public', 'title', 'category',
                  'duration', 'rounds', 'guide', 'user_related',
                  'tag_category', 'tag_user', 'detail'
            ]


class WorkOutCreateSerializer(serializers.Serializer):

    class Meta:
        model = WorkOut
        fields = ['status', 'public', 'title', 'category',
                  'duration', 'rounds', 'guide', 'user_related',
            ]


class WorkOutPartSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkOutParts
        fields = '__all__'