from django.contrib import admin
from .models import Sale, ProductSold, CartItem

admin.site.register(Sale)
admin.site.register(ProductSold)
admin.site.register(CartItem)