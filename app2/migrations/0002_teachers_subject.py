# Generated by Django 5.0.4 on 2024-04-17 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachers',
            name='subject',
            field=models.CharField(default='', max_length=100),
        ),
    ]
