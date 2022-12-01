from django.test import TestCase
from Warehouse.app.models import Category, Product


class ModelTests(TestCase):
    def test_create_category_item(self):
        """Test creating a new category item successfully"""
        # TODO In the future, create tests for deleting and updating items
        category_name = 'Drinks'
        description = 'Drinks - testing purposes'

        Category.objects.create(category_name=category_name,
                                description=description)
        soda = Category.objects.get()

        self.assertEqual(soda.category_name, category_name)
        self.assertEqual(soda.description, description)

    def test_create_product_item(self):
        """Test creating a new product successfully"""
        product_name = 'Coke'
        unit_price = 5.99
        units_in_stock = 10

        Product.objects.create(product_name=product_name,
                               unit_price=unit_price,
                               units_in_stock=units_in_stock)

        coke = Product.objects.get()

        self.assertEqual(coke.product_name, product_name)
        self.assertEqual(coke.unit_price, unit_price)
        self.assertEqual(coke.units_in_stock, units_in_stock)

    def test_create_product_failed(self):
        """Test creating a new product failure"""
        product_name = 'Coke'
        unit_price = '5.99'
        units_in_stock = '10'

        Product.objects.create(product_name=product_name,
                               unit_price=unit_price,
                               units_in_stock=units_in_stock)

        coke = Product.objects.get()

        self.assertNotEqual(coke.unit_price, unit_price)
        self.assertNotEqual(coke.units_in_stock, units_in_stock)



