# Generated by Django 5.0.4 on 2024-05-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app9', '0002_remove_subjects_t_id_subjects_t_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
                ('subjects', models.ManyToManyField(to='app9.subjects')),
            ],
        ),
    ]