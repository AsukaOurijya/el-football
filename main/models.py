import uuid
from django.db import models

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('baju', 'Baju'),
        ('sepatu', 'Sepatu'),
        ('bola', 'Bola'),
        ('merch', 'Merch')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    product_views = models.IntegerField(default=0)


    def __str__(self):
        return self.name

    @property
    def is_product_deals(self):
        return self.product_views > 20

    def increment_views(self):
        self.product_views += 1
        self.save()
