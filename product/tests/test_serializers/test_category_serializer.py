<<<<<<< HEAD
from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title="food")
        self.category_serializer = CategorySerializer(self.category)

    def test_category_serializer(self):
        serializer_data = self.category_serializer.data

=======
from django.test import TestCase

from product.factories import CategoryFactory, ProductFactory
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
    def setUp(self) -> None:
        self.category = CategoryFactory(title="food")
        self.category_serializer = CategorySerializer(self.category)

    def test_category_serializer(self):
        serializer_data = self.category_serializer.data

>>>>>>> pagination
        self.assertEqual(serializer_data["title"], "food")