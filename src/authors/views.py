from typing import Optional

from django.db.models import Q
from rest_framework import viewsets

from src.authors.models import Author
from src.authors.serializers import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

#     # Base
#     def get_queryset(self):
#         user: Optional[int] = self.request.query_params.get("user", None)
#         if user is not None:
#             return Author.objects.filter(user=user)

#         return super().get_queryset()

    # # All names
    # def get_queryset(self):
    #     if (name := self.request.query_params.get("name", None)) is not None:
    #         return Author.objects.filter(
    #             Q(first_name__icontains=name)
    #             | Q(last_name__icontains=name)
    #             | Q(user__name__icontains=name)
    #             | Q(user__username__icontains=name)
    #         )

    #     return super().get_queryset()

    # All names - Improved
    def get_queryset(self):
        qp = self.request.query_params

        param_list = ("first_name", "last_name", "name", "username")
        is_desired_param = any([param in qp for param in param_list])
        if len(qp) > 0 and not is_desired_param:
            return Author.objects.none()

        if (name := qp.get("name", None)) is not None:
            return Author.objects.filter(
                Q(first_name__icontains=name)
                | Q(last_name__icontains=name)
                | Q(user__name__icontains=name)
                | Q(user__username__icontains=name)
            )

        return super().get_queryset()
