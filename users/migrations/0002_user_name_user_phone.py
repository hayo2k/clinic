# Generated by Django 4.2 on 2023-06-03 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=150, null=True),
        ),
    ]