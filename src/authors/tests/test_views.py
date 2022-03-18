import json

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from src.authors.models import Author


class TestAuthorListViewCase(TestCase):
    def setUp(self):
        self.url = reverse("author-list")
        self.author_1 = Author.objects.create(first_name="Name1", last_name="Surname1")
        self.author_2 = Author.objects.create(first_name="Name2", last_name="Surname2")

    def test_serializes_with_correct_data_shape_and_status_code(self):
        """Get all entities"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.json(),
            [
                {
                    "id": self.author_1.id,
                    "first_name": "Name1",
                    "last_name": "Surname1",
                    "full_name": "Name1 Surname1",
                },
                {
                    "id": self.author_2.id,
                    "first_name": "Name2",
                    "last_name": "Surname2",
                    "full_name": "Name2 Surname2",
                },
            ],
        )

    def test_creates_new_author(self):
        """Create single entity"""
        payload = {
            "first_name": "Name3",
            "last_name": "Surname3",
        }
        response = self.client.post(
            self.url, data=json.dumps(payload), content_type="application/json"
        )
        author = Author.objects.last()
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(author)
        self.assertEqual(Author.objects.count(), 3)
        self.assertDictEqual(
            {
                "id": author.id,
                "first_name": "Name3",
                "last_name": "Surname3",
                "full_name": "Name3 Surname3",

            },
            response.json(),
        )


class TestAuthorViewCase(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Name1", last_name="Surname1")
        self.url = reverse("author-detail", kwargs={"pk": self.author.id})

    def test_serializes_single_record_with_correct_data_shape_and_status_code(self):
        """Get single entity"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.json(),
            {
                "id": self.author.id,
                "first_name": "Name1",
                "last_name": "Surname1",
                "full_name": "Name1 Surname1",
            },
        )

    def test_updates_author(self):
        """Update a single entity"""
        payload = {
            "id": self.author.id,
            "first_name": "Name3",
            "last_name": "Surname3",
            "full_name": "Name3 Surname3",
        }
        response = self.client.put(
            self.url, data=json.dumps(payload), content_type="application/json"
        )
        author = Author.objects.filter(id=self.author.id).first()
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(author)
        self.assertEqual(Author.objects.count(), 1)
        self.assertDictEqual(
            {
                "id": author.id,
                "first_name": "Name3",
                "last_name": "Surname3",
                "full_name": "Name3 Surname3",
            },
            response.json(),
        )

    def test_removes_author(self):
        """Delete a single entity"""
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Author.objects.count(), 0)
