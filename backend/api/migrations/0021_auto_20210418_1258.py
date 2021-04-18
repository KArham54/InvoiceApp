# Generated by Django 3.1.7 on 2021-04-18 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_tokenmake'),
    ]

    operations = [
        migrations.AddField(
            model_name='tokenmake',
            name='expiryDate',
            field=models.IntegerField(default=1618766917),
        ),
        migrations.AddField(
            model_name='tokenmake',
            name='salt',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='tokenmake',
            name='token',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='tokenmake',
            name='createdDate',
            field=models.IntegerField(default=1618765117),
        ),
    ]
