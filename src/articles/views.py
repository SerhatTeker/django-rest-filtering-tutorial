from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from src.articles.models import Article
from src.articles.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    )
    filterset_fields = ("id", "title", "regions", "regions__code")
    search_fields = ("id", "title", "regions__name", "regions__code")
    ordering_fields = ("title",)
    ordering = "title"
