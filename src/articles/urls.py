from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from src.articles import views

# Create a router and register our viewsets with it
router = SimpleRouter()
router.register(r"articles", views.ArticleViewSet)

urlpatterns = router.urls
