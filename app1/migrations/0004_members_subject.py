# Generated by Django 5.0.4 on 2024-04-16 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_members_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='subject',
            field=models.CharField(default='', max_length=100),
        ),
    ]
