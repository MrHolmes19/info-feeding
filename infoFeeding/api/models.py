from pyexpat import model
from django.db import models

# Create your models here.
class Ingredient(models.Model):

    class Meta:
        verbose_name = ("ingredient")
        verbose_name_plural = ("s")

    name = models.CharField(max_length=100)
    group = models.CharField(max_length=50)
    subgroup = models.CharField(max_length=50, null=True, blank=True)
    origin = models.CharField(max_length=50, null=True, blank=True)
    commercial_section = models.CharField(max_length=50, null=True, blank=True)

    edible_ptc = models.FloatField(default=1.0)
    density = models.FloatField(null=True, blank=True)
    unit_weight = models.FloatField(null=True, blank=True)
    price_per_gram = models.FloatField(null=True, blank=True)
    calories = models.FloatField()
    proteins = models.FloatField()
    water = models.FloatField(null=True, blank=True)

    sugar = models.FloatField(null=True, blank=True)
    starches = models.FloatField(null=True, blank=True)
    fiber = models.FloatField(null=True, blank=True)
    total_carbohydrates = models.FloatField()

    polyunsaturated_fats = models.FloatField(null=True, blank=True)
    monounsaturated_fats = models.FloatField(null=True, blank=True)
    saturated_fats = models.FloatField(null=True, blank=True)
    trans_fats = models.FloatField(null=True, blank=True)
    total_fats = models.FloatField()
    total_cholesterol = models.FloatField(null=True, blank=True)
    good_cholesterol_HDL = models.FloatField(null=True, blank=True)
    bad_cholesterol_LDL = models.FloatField(null=True, blank=True)

    vitamin_a = models.FloatField(null=True, blank=True)
    vitamin_b1 = models.FloatField(null=True, blank=True)
    vitamin_b2 = models.FloatField(null=True, blank=True)
    vitamin_b3 = models.FloatField(null=True, blank=True)
    vitamin_b12 = models.FloatField(null=True, blank=True)
    vitamin_c = models.FloatField(null=True, blank=True)
    vitamin_d = models.FloatField(null=True, blank=True)
    vitamin_e = models.FloatField(null=True, blank=True)
    vitamin_k = models.FloatField(null=True, blank=True)
    total_vitamins = models.FloatField(null=True, blank=True)

    sodium = models.FloatField(null=True, blank=True)
    potassium = models.FloatField(null=True, blank=True)
    calcium = models.FloatField(null=True, blank=True)
    zinc = models.FloatField(null=True, blank=True)
    iron = models.FloatField(null=True, blank=True)
    phosphorus = models.FloatField(null=True, blank=True)
    magnesium = models.FloatField(null=True, blank=True)
    total_minerals = models.FloatField(null=True, blank=True)
    


    def __str__(self):
        return self.name

