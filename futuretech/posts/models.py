from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Brand(models.Model):
  name = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Seller(models.Model):
  userId = models.OneToOneField(User, on_delete=models.CASCADE)
  publicName = models.CharField(max_length=200)

  def __str__(self):
    return self.publicName

class Post(models.Model):
  class Condition(models.TextChoices):
    NEW = "New"
    USED = "Used"
    REFURBISHED = "Refurbished"

  title = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  condition = models.CharField(choices=Condition.choices, max_length=100)
  categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
  originalPrice = models.DecimalField(max_digits=8, decimal_places=2)
  brandId = models.ForeignKey(Brand, on_delete=models.CASCADE)
  stock = models.IntegerField(default=0)
  sellerId = models.ForeignKey(Seller, on_delete=models.CASCADE)
  discountPercentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

  def __str__(self):
    return self.title

class PostImage(models.Model):
  postId = models.ForeignKey(Post, on_delete=models.CASCADE)
  image = models.BinaryField()

  def __str__(self):
    return self.postId