from django.urls import path
from . import views


urlpatterns = [
    path('home-page', views.HomePageView.as_view()),
    path('parquet-sanding', views.ParquetSandingView.as_view()),
    path('parquet-installation', views.ParquetInstallationView.as_view()),
    path('parquet-refinishing', views.ParquetRefinishingView.as_view()),
    path('local-restoration', views.LocalRestorationView.as_view()),
]