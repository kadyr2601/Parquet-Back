from rest_framework import serializers
from main.models import HomePage

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'
        depth = 1