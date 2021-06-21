from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Skyscraper
from .serializers import SkyscraperSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.

class SkyscraperList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Skyscraper.objects.all()
    serializer_class = SkyscraperSerializer

class SkyscraperDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Skyscraper.objects.all()
    serializer_class = SkyscraperSerializer

