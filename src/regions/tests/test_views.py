import json

from django.test import TestCase
from django.urls import reverse

from src.regions.models import Region


class RegionListViewTestCase(TestCase):
    def setUp(self):
        self.url = reverse("region-list")
        self.region_1 = Region.objects.create(code="DE", name="Germany")
        self.region_2 = Region.objects.create(code="UK", name="United Kingdom")

    def test_serializes_with_correct_data_shape_and_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.json(),
            [
                {
                    "id": self.region_1.id,
                    "code": "DE",
                    "name": "Germany",
                },
                {
                    "id": self.region_2.id,
                    "code": "UK",
                    "name": "United Kingdom",
                },
            ],
        )

    def test_creates_new_region(self):
        payload = {
            "code": "US",
            "name": "United States of America",
        }
        response = self.client.post(
            self.url, data=json.dumps(payload), content_type="application/json"
        )
        region = Region.objects.last()
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(region)
        self.assertEqual(Region.objects.count(), 3)
        self.assertDictEqual(
            {
                "id": region.id,
                "code": "US",
                "name": "United States of America",
            },
            response.json(),
        )


class RegionViewTestCase(TestCase):
    def setUp(self):
        self.region = Region.objects.create(code="DE", name="Germany")
        self.url = reverse("region-detail", kwargs={"pk": self.region.id})

    def test_serializes_single_record_with_correct_data_shape_and_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.json(),
            {
                "id": self.region.id,
                "code": "DE",
                "name": "Germany",
            },
        )

    def test_updates_region(self):
        payload = {
            "id": self.region.id,
            "code": "US",
            "name": "United States of America",
        }
        response = self.client.put(
            self.url, data=json.dumps(payload), content_type="application/json"
        )
        region = Region.objects.filter(id=self.region.id).first()
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(region)
        self.assertEqual(Region.objects.count(), 1)
        self.assertDictEqual(
            {
                "id": region.id,
                "code": "US",
                "name": "United States of America",
            },
            response.json(),
        )

    def test_removes_region(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Region.objects.count(), 0)
