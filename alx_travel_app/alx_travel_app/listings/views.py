from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def hello_world(request):
    return Response({"message": "Welcome to the ALX Travel App API!"})

