# Generated by Django 5.0.4 on 2024-04-18 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0039_alter_attendance_attendance_alter_attendance_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(),
        ),
    ]