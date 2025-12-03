from django.shortcuts import render
from rest_framework import viewsets
from api.models import Task
from api.serilizers import TaskSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
