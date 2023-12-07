from django.contrib import admin
from .models import Post, Category, Brand, Seller, PostImage

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Seller)
admin.site.register(PostImage)
