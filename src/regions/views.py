from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter


from src.regions.models import Region
from src.regions.serializers import RegionSerializer


class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    )
    filterset_fields = ("id", "code")
    search_fields = ("code", "name")
    ordering_fields = ("code",)
    ordering = ("code")
