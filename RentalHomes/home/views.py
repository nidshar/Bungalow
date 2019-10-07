from home import serializers
from home.models import Home
from rest_framework import viewsets

# Create your views here.
class HomeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.HomeSerializer
    queryset = Home.objects.all()