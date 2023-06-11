from django_filters import rest_framework as filters

from src.articles.models import Article


class ArticleFilterSet(filters.FilterSet):
    subject = filters.CharFilter(field_name="title", lookup_expr="exact")

    class Meta:
        model = Article
        fields = ("id", "subject", "regions", "regions__code")

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)
