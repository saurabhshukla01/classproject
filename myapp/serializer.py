from rest_framework.serializers import ModelSerializer
from .models import *


class RestaurantCreateSerializer(ModelSerializer):
    class Meta:
        model = Restaurant    
        fields = '__all__' 

