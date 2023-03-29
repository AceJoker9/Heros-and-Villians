from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import SuperSerializer
from .models import Super



# Create your views here.

@api_view(['GET', 'POST'])
def super_list(request):

    if request.method == 'GET':
        list_of_heros = Super.objects.all()
        serializer = SuperSerializer(supply, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
