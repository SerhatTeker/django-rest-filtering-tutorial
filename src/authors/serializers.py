from rest_framework import serializers

from src.authors.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    # full_name = serializers.CharField(read_only=True, source="full_name")

    class Meta:
        model = Author
        fields = ("id", "user", "first_name", "last_name", "full_name")
        read_only_fields = ("full_name",)
