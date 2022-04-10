from django.urls import path
from src.authors import views


urlpatterns = [
    path(
        "authors/", views.AuthorViewSet.as_view(actions={"get": "list"}), name="authors"
    ),
    # path(
    #     "authors/<int:user>/",
    #     views.AuthorViewSet.as_view(actions={"get": "list"}),
    #     name="authors-by-users",
    # ),
    path(
        "authors/<str:name>/",
        views.AuthorViewSet.as_view(actions={"get": "list"}),
        name="authors-by-first_name",
    ),
    path(
        "authors/<str:last_name>/",
        views.AuthorViewSet.as_view(actions={"get": "list"}),
        name="authors-by-last_name",
    ),
]
