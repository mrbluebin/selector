from rest_framework import serializers
from .models import testnowtime

class testnowtimeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = testnowtime
        fields = ('id','idx','con')