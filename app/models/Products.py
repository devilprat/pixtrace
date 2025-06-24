from django.db import models

from app.models import Accounts


class Products(models.Model):
    name = models.TextField(null=True)
    category = models.TextField(null=True)
    image = models.ImageField()
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'products'
