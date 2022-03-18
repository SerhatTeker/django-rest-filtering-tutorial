from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("src.articles.urls")),
    path("", include("src.authors.urls")),
    path("", include("src.regions.urls")),
    path("", include("src.users.urls")),
]
