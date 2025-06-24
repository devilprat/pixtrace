from django.db import models

from app.models import Products, Accounts


class ProductAnalysis(models.Model):
    year = models.TextField(null=True)
    units_sold = models.TextField(null=True)
    average_rate = models.TextField(null=True)
    sales = models.TextField(null=True)
    growth_rate = models.TextField(null=True)
    market_trend = models.TextField(null=True)
    market_position = models.TextField(null=True)
    market_drivers = models.TextField(null=True)
    market_challenges = models.TextField(null=True)
    remarks = models.TextField(null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_analysis')

    class Meta:
        db_table = 'product_analysis'
