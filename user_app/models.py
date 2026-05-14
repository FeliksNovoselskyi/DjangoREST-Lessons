from django.db import models

class CustomUser(models.Model):
    email = models.EmailField(max_length = 50, unique = True, null = False)
    username = models.CharField(max_length = 50, null = True, unique=True)
    password = models.CharField(max_length = 255, null = False)
