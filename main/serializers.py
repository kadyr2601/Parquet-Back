from rest_framework import serializers
from main.models import HomePage, ParquetSanding, ParquetInstallation, ParquetRefinishing, LocalRestoration

class HomePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        fields = '__all__'
        depth = 1


class ParquetSandingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParquetSanding
        fields = '__all__'


class ParquetInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParquetInstallation
        fields = '__all__'


class ParquetRefinishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParquetRefinishing
        fields = '__all__'


class LocalRestorationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalRestoration
        fields = '__all__'