from django.db import models
from django.core.validators import MaxValueValidator

ChairTypes = [
    ("recliners", "Recliners"),
    ("air_massage", "Air Massage"),
]

Brands = [
    ("kahuna", "Kahuna"),
    ("osaki", "Osaki"),
    ("real_relax", "real Relax"),
]

class ChairFeature(models.Model):
    called = models.CharField(max_length=60)
    def __str__(self):
        return str(self.called)

class ChairType(models.Model):
    called = models.CharField(max_length=60)
    def __str__(self):
        return str(self.called)

class Brand(models.Model):
    brand_name = models.CharField(max_length=20)
    authorized_in = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.authorized_in)

class MassageChair(models.Model):
    title = models.CharField(max_length=35)
    brand = models.CharField(choices=Brands, default=Brands[0], max_length=35)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default=None)
    type = models.CharField(choices=ChairTypes, default=ChairTypes[0], max_length=35)
    purchased = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.6, validators=[MaxValueValidator(limit_value=5.0)])
    posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class ChairComment(models.Model):
    poster = models.CharField(max_length=35, default='Anonymous')
    comment_text = models.TextField(default=None)
    posted_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{str(self.poster)} poster'