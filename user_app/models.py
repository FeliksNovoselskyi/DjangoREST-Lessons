from django.db import models
from django.contrib.auth.models import User


class Car(models.Model):
    
    brand = models.CharField()
    color = models.CharField()
    
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="cars"
    )

class Book(models.Model):
    
    title = models.CharField()
    published_date = models.DateField()
    
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="books"
    )
