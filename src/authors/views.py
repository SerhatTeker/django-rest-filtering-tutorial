from rest_framework import viewsets
from django.db.models import Q

from src.authors.models import Author
from src.authors.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    # User ID
    # def get_queryset(self):
    #     if user := self.kwargs.get("user"):
    #         return Author.objects.filter(user=user)

    #     return super().get_queryset()

    # User name
    # def get_queryset(self):
    #     if name := self.kwargs.get("name"):
    #         return Author.objects.filter(user__name__icontains=name)

    #     return super().get_queryset()

    # Any Name
    def get_queryset(self):
        if name := self.kwargs.get("name"):
            return Author.objects.filter(
                Q(first_name__icontains=name)
                | Q(last_name__icontains=name)
                | Q(user__name__icontains=name)
                | Q(user__username__icontains=name)
            )

        return super().get_queryset()
