# Generated by Django 4.1.7 on 2023-03-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.FloatField(null=True),
        ),
    ]