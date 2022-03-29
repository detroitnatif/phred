from django.shortcuts import render
from rest_framework import viewsets
from .models import dataObj
from 
from .serializers import ReactSerializer


class dataObjView(viewsets.ModelViewSet):
    serializer_class = ReactSerializer
    queryset = dataObj.objects.all()
# Create your views here.
