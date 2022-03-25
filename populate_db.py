# type: ignore
# flake8: noqa
import django
import logging
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", ".."))
django.setup()

from src.articles.models import Article
from src.regions.models import Region
from src.authors.models import Author
from src.users.models import User
from django.core import management

# Migrate
management.call_command("migrate", no_input=True)

# Seed

# users
user_1 = User.objects.create(username="User1", name="UserName1")
user_2 = User.objects.create(username="User2", name="UserName2")
user_3 = User.objects.create(username="User3", name="UserName3")

# authors
author_1 = Author.objects.create(user=user_1, first_name="Name1", last_name="Surname1")
author_2 = Author.objects.create(first_name="Name2", last_name="Surname2")
author_3 = Author.objects.create(user=user_3, first_name="Name3", last_name="Surname3")

# regions
region_de = Region.objects.create(code="DE", name="Germany")
region_uk = Region.objects.create(code="UK", name="United Kingdom")

# Articles

# articles with author without regions
Article.objects.create(title="Fake Article1", content="Fake Content1", author=author_1)
Article.objects.create(title="Fake Article2", content="Fake Content2", author=author_2)
Article.objects.create(title="Fake Article3", content="Fake Content3", author=author_3)

# articles with regions
Article.objects.create(title="Fake Article4", content="Fake Content5").regions.set(
    [
        Region.objects.create(code="CA", name="Canadia"),
        Region.objects.create(code="AU", name="Australia"),
    ]
)
Article.objects.create(title="Fake Article5", content="Fake Content5").regions.set(
    [
        Region.objects.create(code="IT", name="Italy"),
        Region.objects.create(code="CH", name="Switzerland"),
    ]
)
# articles with author and regions
for index in range(6, 11):
    Article.objects.create(
        title=f"Fake Article{index}", content=f"Fake Content{index}", author=author_3
    ).regions.set([region_de.id, region_uk.id])

logging.info("Database populated with dummy data.")
