# Generated by Django 5.0.4 on 2024-04-16 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_members_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
