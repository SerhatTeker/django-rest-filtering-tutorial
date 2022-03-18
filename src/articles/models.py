from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    regions = models.ManyToManyField("regions.Region", blank=True)
    author = models.ForeignKey(
        "authors.Author",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        author = self.author or "Unknown"
        return f"{self.title} by {author}"
