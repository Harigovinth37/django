# Generated by Django 5.0.4 on 2024-04-15 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('section', models.CharField(max_length=10)),
                ('contact', models.IntegerField()),
            ],
        ),
    ]