from django.shortcuts import render 
from rest_framework import viewsets
from .serializers import AnSerializer
from .models import An

class AnViewSet(viewsets.ModelViewSet):
    queryset = An.objects.all()
    serializer_class = AnSerializer
    #pagination
    #permissions class
    
    #get_queryset avec User
    
    #get_serializer_context
    
    #perform_create