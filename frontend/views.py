from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def homepage_api(request, format=None):
    return Response({
        'exercises': reverse('exercise:homepage', format=None, request=request),
        'workouts': reverse('workout:homepage', format=None, request=request),
        'accounts': reverse('accounts:homepage', format=None, request=request),
        'planner': reverse('planner:homepage', format=None, request=request),
    })

