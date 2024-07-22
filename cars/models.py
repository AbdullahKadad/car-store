from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Car(models.Model):
    buyer_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    model = models.CharField(max_length=35, blank=False, null=False)
    brand = models.CharField(max_length=255, blank=False, null=False)
    price = models.FloatField(blank=False, null=False, default=0.0)
    is_bought = models.BooleanField(default=False)
    buy_time = models.DateField()

    def __str__(self):
        return f"{self.model} by {self.brand} at ${self.price}"
