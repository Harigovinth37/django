# Generated by Django 5.0.4 on 2024-04-18 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_remove_attendance_class_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feesdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentName', models.CharField(max_length=100)),
                ('className', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]