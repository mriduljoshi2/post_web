from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://cdni.iconscout.com/illustration/premium/thumb/server-down-of-restaurant-website-illustration-download-in-svg-png-gif-file-formats--404-error-not-found-page-food-delivery-pack-e-commerce-shopping-illustrations-3605234.png?f=webp")