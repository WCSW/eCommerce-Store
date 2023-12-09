from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self) -> None:
        self.data1 = Category.objects.create(name="testCategoryName", slug="testCategoryName")

    def test_category_model_entry(self):
        """
        Test Category models data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), "testCategoryName")


class TestProductModel(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name="testCategory", slug="testCategory")
        User.objects.create(username="admin")
        self.data1 = Product.objects.create(
            category_id=1,
            title="testProduct1",
            created_by_id=1,
            slug="testProduct1",
            price=20.00,
            image="testProduct1Image",
        )

    def test_product_model_entry(self):
        """
        Test Category models data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), "testProduct1")
