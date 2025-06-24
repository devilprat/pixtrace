from django.db import models

from app.models import Products, Accounts


class ProductReview(models.Model):
    platform = models.TextField(null=True)
    link = models.TextField(null=True)
    author = models.TextField(null=True)
    caption = models.TextField(null=True)
    engagement = models.TextField(null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='product_review')

    class Meta:
        db_table = 'product_review'
