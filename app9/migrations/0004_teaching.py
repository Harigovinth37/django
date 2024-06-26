# Generated by Django 5.0.4 on 2024-05-02 11:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app9', '0003_classes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teaching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app9.classes')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app9.subjects')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app9.tregistration')),
            ],
        ),
    ]
