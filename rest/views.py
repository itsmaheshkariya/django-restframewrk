from django.shortcuts import render
from .serializer import BloggerSerializer
from rest_framework import viewsets
from .models import Blogger
class BloggerViewSet(viewsets.ModelViewSet):
    queryset = Blogger.objects.all()
    serializer_class = BloggerSerializer