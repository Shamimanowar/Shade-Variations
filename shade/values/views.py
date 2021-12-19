from django.shortcuts import render
from .models import ShadeVariation
from .serializers import ShadeSerializer
from rest_framework import generics

# Create your views here.

class ShadeListCreate(generics.ListCreateAPIView):
    queryset = ShadeVariation.objects.all()
    serializer_class = ShadeSerializer


class ShadeRetrievUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShadeVariation
    serializer_class = ShadeSerializer
    lookup_field = 'id'
