# Generated by Django 5.0.4 on 2024-04-18 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_feesdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
