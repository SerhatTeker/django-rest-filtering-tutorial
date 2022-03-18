from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from src.users.serializers import User, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    )
    filterset_fields = ("id", "username")
    search_fields = ("id", "username")
    ordering_fields = ("username",)
    ordering = "username"

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = self.serializer_class(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
