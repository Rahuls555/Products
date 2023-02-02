from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField( max_length=50)
    description=models.TextField()
    price=models.DecimalField(max_digits=50, decimal_places=6)

    def __str__(self):
        return 'Massage From ' + self.name +' - ' +self.price
    