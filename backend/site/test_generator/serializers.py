from rest_framework.serializers import *
from .models import Option

class OptionSerializer(ModelSerializer):
    class Meta:
        model = Option
        fields = ['__all__']