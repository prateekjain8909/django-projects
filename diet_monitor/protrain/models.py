# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Nutrition(models.Model):
    food = models.TextField(db_column='Food')  # Field name made lowercase.
    calories = models.TextField(db_column='Calories', blank=True, null=True)  # Field name made lowercase.
    total_fat = models.TextField(db_column='Total_Fat', blank=True, null=True)  # Field name made lowercase.
    saturated_fat = models.TextField(db_column='Saturated_Fat', blank=True, null=True)  # Field name made lowercase.
    polyunsaturated_fat = models.TextField(db_column='Polyunsaturated_Fat', blank=True, null=True)  # Field name made lowercase.
    monounsaturated_fat = models.TextField(db_column='Monounsaturated_Fat', blank=True, null=True)  # Field name made lowercase.
    cholesterol = models.TextField(db_column='Cholesterol', blank=True, null=True)  # Field name made lowercase.
    sodium = models.TextField(db_column='Sodium', blank=True, null=True)  # Field name made lowercase.
    potassium = models.TextField(db_column='Potassium', blank=True, null=True)  # Field name made lowercase.
    total_carbohydrate = models.TextField(db_column='Total_Carbohydrate', blank=True, null=True)  # Field name made lowercase.
    dietary_fiber = models.TextField(db_column='Dietary_Fiber', blank=True, null=True)  # Field name made lowercase.
    sugars = models.TextField(db_column='Sugars', blank=True, null=True)  # Field name made lowercase.
    protein = models.TextField(db_column='Protein', blank=True, null=True)  # Field name made lowercase.
    vitamin_a = models.TextField(db_column='Vitamin_A', blank=True, null=True)  # Field name made lowercase.
    vitamin_b12 = models.TextField(db_column='Vitamin_B12', blank=True, null=True)  # Field name made lowercase.
    vitamin_b6 = models.TextField(db_column='Vitamin_B6', blank=True, null=True)  # Field name made lowercase.
    vitamin_c = models.TextField(db_column='Vitamin_C', blank=True, null=True)  # Field name made lowercase.
    vitamin_d = models.TextField(db_column='Vitamin_D', blank=True, null=True)  # Field name made lowercase.
    vitamin_e = models.TextField(db_column='Vitamin_E', blank=True, null=True)  # Field name made lowercase.
    calcium = models.TextField(db_column='Calcium', blank=True, null=True)  # Field name made lowercase.
    copper = models.TextField(db_column='Copper', blank=True, null=True)  # Field name made lowercase.
    folate = models.TextField(db_column='Folate', blank=True, null=True)  # Field name made lowercase.
    iron = models.TextField(db_column='Iron', blank=True, null=True)  # Field name made lowercase.
    magnesium = models.TextField(db_column='Magnesium', blank=True, null=True)  # Field name made lowercase.
    manganese = models.TextField(db_column='Manganese', blank=True, null=True)  # Field name made lowercase.
    niacin = models.TextField(db_column='Niacin', blank=True, null=True)  # Field name made lowercase.
    pantothenic_acid = models.TextField(db_column='Pantothenic_Acid', blank=True, null=True)  # Field name made lowercase.
    phosphorus = models.TextField(db_column='Phosphorus', blank=True, null=True)  # Field name made lowercase.
    riboflavin = models.TextField(db_column='Riboflavin', blank=True, null=True)  # Field name made lowercase.
    selenium = models.TextField(db_column='Selenium', blank=True, null=True)  # Field name made lowercase.
    thiamin = models.TextField(db_column='Thiamin', blank=True, null=True)  # Field name made lowercase.
    zinc = models.TextField(db_column='Zinc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Nutrition'


class Recipie(models.Model):
    food = models.TextField(db_column='Food', blank=True, null=True)  # Field name made lowercase.
    servings = models.IntegerField(db_column='Servings', blank=True, null=True)  # Field name made lowercase.
    ingredients = models.TextField(db_column='Ingredients', blank=True, null=True)  # Field name made lowercase.
    procedure = models.TextField(db_column='Procedure', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Recipie'
