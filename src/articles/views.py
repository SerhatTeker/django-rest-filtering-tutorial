from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from src.articles.filters import ArticleFilterSet
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
    filterset_class = ArticleFilterSet
    search_fields = ("id", "title", "regions__name", "regions__code")
    ordering_fields = ("title",)
    ordering = "title"

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)
