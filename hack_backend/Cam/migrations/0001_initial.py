# Generated by Django 4.2.7 on 2023-11-18 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pixelWidth', models.FloatField()),
                ('pixelLength', models.FloatField()),
            ],
        ),
    ]
