# Generated by Django 4.1.7 on 2023-03-05 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=255)),
                ('Email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]