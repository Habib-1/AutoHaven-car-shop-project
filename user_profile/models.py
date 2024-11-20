from django.db import models
from django.contrib.auth.models import User
from product.models import car
# Create your models here.
class purchase(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(car,on_delete=models.CASCADE)
    purchased_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}  {self.product}  {self.purchased_at}"
