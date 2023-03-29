from django.shortcuts import render
from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import Super_typesSerializer
from .models import Super_types

# Create your views here.

@api_view(['GET', 'POSST'])
def choice_super(request):

    if request.method == 'GET':
        good_or_evil = Super_types.objects.all()
        serializer = Super_typesSerializer(supply, many=True)
        return Response(serializer.data)
    
    elif request.methood == 'POST':
        serializer = Super_typesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


