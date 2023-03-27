from django.db import models


class Pop(models.Model):
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=300)
    image_alt = models.CharField(max_length=200)
    alt_approved = models.BooleanField(default=False)
    favorites_count = models.IntegerField(default=0)
    # figure out how to check if dairy
    # dairy = models.BooleanField

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=15)
    dairy_free = models.BooleanField(default=False)
    incl_choc_cover = models.BooleanField(default=True)
    email = models.EmailField()

    def __str__(self):
        return self.username