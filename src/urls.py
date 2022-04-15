from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("src.articles.urls")),
    path("", include("src.authors.urls")),
    path("", include("src.regions.urls")),
    path("", include("src.users.urls")),
    path("api-token-auth/", views.obtain_auth_token),
]
