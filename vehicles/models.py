from django.db import models
from PIL import Image

class vehicles(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    mileage = models.DecimalField(max_digits=12, decimal_places=2)
    picture = models.ImageField(upload_to= 'img', blank=True, null=True)

    def __str__(self):
        return "{}{}".format(self.brand, self.model)
    
    
class Transaction(models.Model):
    buyer = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='purchases')
    seller = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='transaction')
    vehicle = models.ForeignKey(vehicles, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2)


