from django.db.models import Q
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from src.authors.models import Author
from src.authors.serializers import AuthorSerializer


class AuthorFilter(filters.FilterSet):
    # full_name = filters.CharFilter(field_name="full_name", label="full_name", lookup_expr="contains")
    full_name = filters.CharFilter(label="full_name", method="search_in_names")

    class Meta:
        model = Author
        fields = ("id", "user", "first_name", "last_name")

    @staticmethod
    def search_in_names(queryset, name, value):
        for term in value.split():
            qs = queryset.filter(
                Q(first_name__icontains=term) | Q(last_name__icontains=term)
            )

        return qs


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filter_backends = (
        filters.DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    )
    filterset_class = AuthorFilter
    search_fields = ("full_name", "first_name", "last_name")
    ordering_fields = ("first_name", "last_name")
    ordering = "last_name"
