from django.db import models

# Create your models here.
class brand(models.Model):
    brand_name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True, blank=True, null=True)
    def __str__(self):
        return f"{self.brand_name} {self.slug}"
    
class car(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    brand=models.ForeignKey(brand, on_delete=models.CASCADE,related_name='car_brand')
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        return f"Name : {self.name} , Brand : {self.brand}"

class Comments(models.Model):
    car=models.ForeignKey(car,on_delete=models.CASCADE,related_name='comment')
    name=models.CharField(max_length=50)
    email=models.EmailField()
    comment_text=models.TextField()
    comment_time=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    def __str__(self):
        return self.name