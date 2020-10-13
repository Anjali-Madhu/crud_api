from django.shortcuts import render
from .models import *
from  .serializers import *

# Create your views here.

from rest_framework import viewsets


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
