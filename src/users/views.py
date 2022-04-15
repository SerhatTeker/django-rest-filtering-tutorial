from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from src.users.serializers import CreateUserSerializer, User, UserSerializer


class UserModelViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.
        """
        if self.action == "create":
            return CreateUserSerializer
        return UserSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "create":
            return [AllowAny()]

        return super().get_permissions()

    @action(detail=False, methods=["GET"])
    def me(self, request):
        serializer = self.serializer_class(request.user, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)
