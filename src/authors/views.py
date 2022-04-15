from django.db.models import Q
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from src.authors.models import Author
from src.authors.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    # def get_queryset(self):
    #     user = self.request.query_params.get("user", None)
    #     if user is not None:
    #         return Author.objects.filter(user=user)

    #     return super().get_queryset()

    def get_queryset(self):
        params = ("user", "user_id")
        if not all([param in self.request.query_params for param in params]):
            return Author.objects.none()

        user = self.request.query_params.get("user", None)
        user_id = self.request.query_params.get("user_id", None)
        user = user or user_id

        if user is not None:
            return Author.objects.filter(user=user)

        return super().get_queryset()
