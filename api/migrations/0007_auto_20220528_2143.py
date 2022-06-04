# Generated by Django 3.2.9 on 2022-05-28 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20220301_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='allowed_units',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='cooking',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='presentation',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
