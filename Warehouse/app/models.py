from django.db import models


class Category(models.Model):
    """Model for a categories table in Northwind database"""
    category_name = models.CharField(max_length=25)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """
    SENIORITY = [
        ('JUNIOR', 'Junior'),
        ('MID', 'Middle'),
        ('SENIOR', 'Senior'),
    ]"""
    """Model for a products table in Northwind database"""
    product_name = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    unit_price = models.FloatField(default=0)
    units_in_stock = models.IntegerField(default=0)
    """choices = models.CharField(max_length=20,choices=SENIORITY, default='Junior')"""

    def __str__(self):
        return self.product_name
