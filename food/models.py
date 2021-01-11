from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc =models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://www.flaticon.com/svg/static/icons/svg/1377/1377194.svg')
    def __str__(self):
        return self.item_name