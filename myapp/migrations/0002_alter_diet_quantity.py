# Generated by Django 5.1.6 on 2025-03-16 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diet',
            name='quantity',
            field=models.CharField(max_length=100),
        ),
    ]
