from django.urls import path
from . import views


urlpatterns = [
    path('home-page', views.HomePageView.as_view()),
]