# Generated by Django 4.2.3 on 2023-09-08 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateField(),
        ),
    ]
