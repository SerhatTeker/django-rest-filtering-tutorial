from django.urls import path, include
from rest_framework.routers import DefaultRouter
from src.regions import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r"regions", views.RegionViewSet)

urlpatterns = router.urls
