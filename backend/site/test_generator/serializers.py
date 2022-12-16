from rest_framework.serializers import *
from .models import Option, Task

class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = ['__all__']

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ['option']