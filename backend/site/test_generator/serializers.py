from rest_framework.serializers import *
from .models import Option, Task

class OptionFileSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = ['decision']

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        exclude = ['option']