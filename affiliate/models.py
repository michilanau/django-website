from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to="products", blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
    	try:
    		url = self.image.url
    		print(url)
    	except:
    		url = ''
    	return url