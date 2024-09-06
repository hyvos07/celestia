from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
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

    def __str__(self):
        return self.name
