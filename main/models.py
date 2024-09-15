import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    chara = models.CharField(max_length=255)
    game = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    # image = models.ImageField(upload_to='images/', null=True, blank=True)
    image = models.TextField(max_length=255)
    
    @property
    def image_URL(self):
        try:
            url = self.image.url
            if url == None:
                assert Exception
        except:
            url = r'..\..\assets\dev\Error.png'
        return url
    
    @property
    def price_with_comma(self):
        return "{:,}".format(self.price)
    
    @property
    def is_stock_empty(self):
        return self.stock == 0

    def __str__(self):
        return self.name
