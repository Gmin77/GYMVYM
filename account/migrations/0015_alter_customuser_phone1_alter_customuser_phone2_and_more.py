# Generated by Django 5.0.3 on 2024-07-25 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_remove_customuser_phone_number_customuser_phone1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone1',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone2',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone3',
            field=models.CharField(max_length=4),
        ),
    ]
