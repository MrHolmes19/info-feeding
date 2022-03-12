# Generated by Django 3.2.9 on 2022-03-01 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_ingredient_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.CharField(default=None, max_length=100, null=True)),
                ('cooking_time', models.FloatField(blank=True, null=True)),
                ('difficulty', models.FloatField(blank=True, null=True)),
                ('portions', models.FloatField()),
                ('recipe', models.TextField(blank=True, null=True)),
                ('image', models.FileField(null=True, upload_to='media/')),
                ('total_price', models.FloatField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=50, null=True)),
                ('group', models.CharField(blank=True, max_length=50, null=True)),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('subfoods', models.TextField(blank=True, null=True)),
                ('calories', models.FloatField()),
                ('proteins', models.FloatField()),
                ('water', models.FloatField(blank=True, null=True)),
                ('sugar', models.FloatField(blank=True, null=True)),
                ('starches', models.FloatField(blank=True, null=True)),
                ('fiber', models.FloatField(blank=True, null=True)),
                ('total_carbohydrates', models.FloatField()),
                ('polyunsaturated_fats', models.FloatField(blank=True, null=True)),
                ('monounsaturated_fats', models.FloatField(blank=True, null=True)),
                ('saturated_fats', models.FloatField(blank=True, null=True)),
                ('trans_fats', models.FloatField(blank=True, null=True)),
                ('total_fats', models.FloatField()),
                ('total_cholesterol', models.FloatField(blank=True, null=True)),
                ('good_cholesterol_HDL', models.FloatField(blank=True, null=True)),
                ('bad_cholesterol_LDL', models.FloatField(blank=True, null=True)),
                ('vitamin_a', models.FloatField(blank=True, null=True)),
                ('vitamin_b1', models.FloatField(blank=True, null=True)),
                ('vitamin_b2', models.FloatField(blank=True, null=True)),
                ('vitamin_b3', models.FloatField(blank=True, null=True)),
                ('vitamin_b12', models.FloatField(blank=True, null=True)),
                ('vitamin_c', models.FloatField(blank=True, null=True)),
                ('vitamin_d', models.FloatField(blank=True, null=True)),
                ('vitamin_e', models.FloatField(blank=True, null=True)),
                ('vitamin_k', models.FloatField(blank=True, null=True)),
                ('total_vitamins', models.FloatField(blank=True, null=True)),
                ('sodium', models.FloatField(blank=True, null=True)),
                ('potassium', models.FloatField(blank=True, null=True)),
                ('calcium', models.FloatField(blank=True, null=True)),
                ('zinc', models.FloatField(blank=True, null=True)),
                ('iron', models.FloatField(blank=True, null=True)),
                ('phosphorus', models.FloatField(blank=True, null=True)),
                ('magnesium', models.FloatField(blank=True, null=True)),
                ('total_minerals', models.FloatField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'food',
                'verbose_name_plural': 'foods',
            },
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'ingredient', 'verbose_name_plural': 'ingredients'},
        ),
        migrations.AddField(
            model_name='ingredient',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to='media/'),
        ),
    ]