from rest_framework import serializers

from src.articles.models import Article
from src.regions.models import Region
from src.regions.serializers import RegionSerializer


class ArticleSerializer(serializers.ModelSerializer):
    regions = RegionSerializer(many=True)

    class Meta:
        model = Article
        fields = ("id", "author", "title", "content", "regions")

    def create(self, validated_data):
        regions_data = validated_data.pop("regions")
        article = Article.objects.create(**validated_data)
        for data in regions_data:
            region, _ = Region.objects.get_or_create(**data)
            article.regions.add(region)

        return article
