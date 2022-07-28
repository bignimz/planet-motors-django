from email.policy import default
from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.

class Car(models.Model):

    year_choice = []
    for r in range(2010, (datetime.now().year + 1)):
        year_choice.append((r, r))

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('Park Assist', 'Park Assist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Sunroof', 'Sunroof'),
        ('Bluetooth Handset', 'Bluetooth Handset')
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    car_title = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', default='media/photos/default.jpg')
    photo_7 = models.ImageField(upload_to='photos/%Y/%m/%d/', default='media/photos/default.jpg')
    photo_8 = models.ImageField(upload_to='photos/%Y/%m/%d/', default='media/photos/default.jpg')
    photo_9 = models.ImageField(upload_to='photos/%Y/%m/%d/', default='media/photos/default.jpg')
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    doors = models.CharField(choices=door_choices, max_length=10)
    seats = models.IntegerField(max_length=10)
    reg_number = models.CharField(max_length=155)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title


