# Generated by Django 3.1.7 on 2021-04-16 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='', upload_to='media/faces/%Y/%m/%d/'),
        ),
    ]
