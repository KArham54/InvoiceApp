# Generated by Django 3.1.7 on 2021-04-18 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_auto_20210418_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokenmake',
            name='createdDate',
            field=models.IntegerField(default=1618766023),
        ),
        migrations.AlterField(
            model_name='tokenmake',
            name='expiryDate',
            field=models.IntegerField(default=1618767823),
        ),
        migrations.AlterField(
            model_name='tokenmake',
            name='salt',
            field=models.CharField(default='1011b218a8d7494', max_length=500),
        ),
    ]
