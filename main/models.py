import uuid
from django.db import models

# Create your models here.

class footballShop(models.Model):
    CATEGORY_CHOICES = []

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField()
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField()
    is_featured = models.BooleanField()