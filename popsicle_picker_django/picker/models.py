from django.db import models

# Create your models here.

class Pop(models.model):
    name = models.CharField
    image = models.ImageField
    image_alt = models.CharField
    favorites_count = models.IntegerField(default=0)
    # figure out how to check if dairy
    # dairy = models.BooleanField


class User(models.model):
    username = models.CharField(max_length=15)
    # favorites = models.list of foreign keys ? 
    # dislikes = models.list of foreign keys ?
    dairy_free = models.BooleanField
    incl_choc_cover = models.BooleanField  
    # will probably need:
    email = models.EmailField  