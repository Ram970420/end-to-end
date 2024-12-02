from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import path
from . import views  

@api_view(['GET'])
def get_message(request):
    return Response({"message": "Hello from Django backend!"})

@api_view(['POST'])
def post_message(request):
    data = request.data
    return Response({"response": f"Received: {data.get('input')}"})

urlpatterns = [
    path('example/', views.example_view, name='example'),
]

