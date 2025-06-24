from django.db import models

from app.models import Products, Accounts


class CompetitorAnalysis(models.Model):
    brand = models.TextField(null=True)
    model = models.TextField(null=True)
    average_price = models.TextField(null=True)
    target_audience = models.TextField(null=True)
    key_features = models.TextField(null=True)
    strengths = models.TextField(null=True)
    weaknesses = models.TextField(null=True)
    market_share_estimate = models.TextField(null=True)
    positioning = models.TextField(null=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    class Meta:
        db_table = 'competitor_analysis'
