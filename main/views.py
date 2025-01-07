from rest_framework import views, response
from main.models import HomePage, ParquetSanding, ParquetInstallation, ParquetRefinishing, LocalRestoration
from main.serializers import (HomePageSerializer, ParquetSandingSerializer, ParquetInstallationSerializer,
                              ParquetRefinishingSerializer, LocalRestorationSerializer)


class HomePageView(views.APIView):
    def get(self, request):
        home_page = HomePage.objects.first()
        serializer = HomePageSerializer(home_page)
        return response.Response(serializer.data)


class ParquetSandingView(views.APIView):
    def get(self, request):
        parquet_sanding = ParquetSanding.objects.first()
        serializer = ParquetSandingSerializer(parquet_sanding)
        return response.Response(serializer.data)


class ParquetInstallationView(views.APIView):
    def get(self, request):
        parquet_installation = ParquetInstallation.objects.all()
        serializer = ParquetInstallationSerializer(parquet_installation, many=True)
        return response.Response(serializer.data)


class ParquetRefinishingView(views.APIView):
    def get(self, request):
        parquet_refinishing = ParquetRefinishing.objects.first()
        serializer = ParquetRefinishingSerializer(parquet_refinishing)
        return response.Response(serializer.data)


class LocalRestorationView(views.APIView):
    def get(self, request):
        local_restoration = LocalRestoration.objects.first()
        serializer = LocalRestorationSerializer(local_restoration)
        return response.Response(serializer.data)