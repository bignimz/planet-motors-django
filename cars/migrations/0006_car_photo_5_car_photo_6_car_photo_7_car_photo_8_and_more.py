# Generated by Django 4.0.4 on 2022-07-28 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_main_photo_alter_car_photo_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='photo_5',
            field=models.ImageField(default='default.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo_6',
            field=models.ImageField(default='default.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo_7',
            field=models.ImageField(default='default.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo_8',
            field=models.ImageField(default='default.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo_9',
            field=models.ImageField(default='default.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
    ]