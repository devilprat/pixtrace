from django.db import models

from app.models import Products, Accounts


class Distributor(models.Model):
    name = models.TextField(null=True)
    address = models.TextField(null=True)
    contact = models.TextField(null=True)
    email = models.TextField(null=True)
    website = models.TextField(null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='distributors')

    class Meta:
        db_table = 'distributor'
