from django.db import models
from django.core.validators import MaxValueValidator
from django.utils import timezone

def RetrieveDate(Raw_Date):
    day = Raw_Date.day
    month = Raw_Date.month
    year = Raw_Date.year
    return day, month, year

ChairTypes = [
    ("recliners", "Recliners"),
    ("air_massage", "Air Massage"),
]

Brands = [
    ("kahuna", "Kahuna"),
    ("osaki", "Osaki"),
    ("real_relax", "real Relax"),
]
Colors = [
    ("Red", "Red"),
    ("Blue", "Blue"),
    ("Black", "Black"),
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
        return str(self.brand_name)

class MassageChair(models.Model):
    title = models.CharField(max_length=35)
    brand = models.OneToOneField(Brand, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(default=None)
    available_colors = models.ManyToManyField('Color_Options', related_name='massage_chairs')
    features = models.ManyToManyField(ChairFeature, related_name='Massage_Features')
    purchased = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.6, validators=[MaxValueValidator(limit_value=5.0)])
    posted = models.DateTimeField(default=timezone.now)

    def color_options(self):
        colors = self.available_colors.all()
        return [[str(color.color_name), str(color.color_code), str(color.image.url)] for color in colors]
    
    def chair_features(self):
        features = self.features.all()
        return [str(feature.called) for feature in features]
    
    def posted(self):
        return 'today'

    def __str__(self):
        return str(self.title)

class ChairComment(models.Model):
    posted_for = models.ForeignKey(MassageChair, on_delete=models.CASCADE)
    poster = models.CharField(max_length=35, default='Anonymous')
    comment_text = models.TextField(default=None)
    posted_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{str(self.poster)} poster'

class Color_Options(models.Model):
    color_name = models.CharField(max_length=50, unique=True)
    color_code = models.TextField()
    image = models.ImageField(default=None, blank=True, null=True)
    def __str__(self):
        return self.color_name
    
    class Meta:
        verbose_name_plural = "Chair Colors"