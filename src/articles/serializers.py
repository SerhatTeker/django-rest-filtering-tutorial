from rest_framework import serializers

from src.articles.models import Article
from src.regions.serializers import RegionSerializer


class ArticleSerializer(serializers.ModelSerializer):
    regions = RegionSerializer(many=True)

    class Meta:
        model = Article
        fields = ("id", "author", "title", "content", "regions")
