from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Sale(models.Model):
  userId = models.ForeignKey(User, on_delete=models.CASCADE)
  isPaid = models.BooleanField(default=False)
  
  def __str__(self):
    return self.userId.username

class ProductSold(models.Model):
  postId = models.ForeignKey(Post, on_delete=models.CASCADE)
  saleId = models.ForeignKey(Sale, on_delete=models.CASCADE)
  pricePerunit = models.DecimalField(max_digits=8, decimal_places=2)
  amount = models.PositiveIntegerField(default=1)

  def __str__(self):
    return self.postId.title + '- by ' + self.saleId.userId.username
  
  def get_total_price(self):
    return self.pricePerunit * self.amount
  