# Generated by Django 3.2.9 on 2022-02-27 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_ingredient_sodium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
