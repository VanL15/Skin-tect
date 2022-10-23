from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/')

    @classmethod
    def create(cls, name):
        Image = cls(name=name)
        return Image

    def __str__(self):
        return self.name