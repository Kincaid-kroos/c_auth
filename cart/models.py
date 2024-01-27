from django.db import models
from datetime import datetime

class cartItems(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')
    available = models.IntegerField()
    amount = models.IntegerField()
    latest = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=datetime.now, blank=True)


    
    def __str__(self):
        return self.name
