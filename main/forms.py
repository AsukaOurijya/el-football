from django.forms import ModelForm
from main.models import product

class ProductForm(ModelForm):
    class Meta:
        model = product
        fields = ["name", "price", "description", "category", "thumbnail", "is_featured"]