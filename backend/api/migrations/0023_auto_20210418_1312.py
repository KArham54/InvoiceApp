# Generated by Django 3.1.7 on 2021-04-18 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20210418_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tokenmake',
            name='createdDate',
            field=models.IntegerField(default=1618765976),
        ),
        migrations.AlterField(
            model_name='tokenmake',
            name='expiryDate',
            field=models.IntegerField(default=1618767776),
        ),
        migrations.AlterField(
            model_name='tokenmake',
            name='salt',
            field=models.CharField(default='<sha256 _hashlib.HASH object @ 0x10d3b59b0>', max_length=500),
        ),
    ]