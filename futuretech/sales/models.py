from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Sale(models.Model):
  userId = models.ForeignKey(User, on_delete=models.CASCADE)
  address = models.CharField(max_length=200)
  isPaid = models.BooleanField(default=False)

  def __str__(self):
    return self.userId + " " + self.isPaid

class ProductSold(models.Model):
  postId = models.ForeignKey(Post, on_delete=models.CASCADE)
  saleId = models.ForeignKey(Sale, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=0)
  pricePerunit = models.DecimalField(max_digits=8, decimal_places=2)
  amount = models.IntegerField(default=1)
