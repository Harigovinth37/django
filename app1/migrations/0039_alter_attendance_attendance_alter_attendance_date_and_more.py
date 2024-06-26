# Generated by Django 5.0.4 on 2024-04-18 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0038_alter_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='section',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='standard',
            field=models.CharField(max_length=100),
        ),
    ]
