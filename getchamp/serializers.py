from rest_framework import serializers
from .models import *

class ChampionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Champion
        fields = ['Name','Image','Class','Origin','Money']