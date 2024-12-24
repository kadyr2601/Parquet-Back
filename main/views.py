from rest_framework import views, response
from main.models import HomePage
from main.serializers import HomePageSerializer


class HomePageView(views.APIView):
    def get(self, request):
        home_page = HomePage.objects.first()
        serializer = HomePageSerializer(home_page)
        return response.Response(serializer.data)