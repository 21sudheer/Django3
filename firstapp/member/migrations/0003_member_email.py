# Generated by Django 4.1.7 on 2023-03-01 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
