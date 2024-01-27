from django.db import models
from datetime import datetime

class ReviewsItems(models.Model):
    name = models.CharField(max_length=50)
    comments = models.CharField(max_length=500)
    


    
    def __str__(self):
        return self.name
