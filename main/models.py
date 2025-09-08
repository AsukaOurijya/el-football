import uuid
from django.db import models

# Create your models here.

class product(models.Model):
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