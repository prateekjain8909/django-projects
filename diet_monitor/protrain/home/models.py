from django.db import models

# Create your models here.

class Nutrition(models.Model):
    food = models.TextField(db_column='Food')  # Field name made lowercase.
    servings = models.IntegerField(db_column='Servings', blank=True, null=True)  # Field name made lowercase.
    ingredients = models.TextField(db_column='Ingredients', blank=True, null=True)  # Field name made lowercase.
    procedure = models.TextField(db_column='Procedure', blank=True, null=True)  # Field name made lowercase.
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

    def fill(self, item):
        self.food = item[0] 
        self.ingredients = item[1] 
        self.procedure = item[2] 
        self.servings = item[3] 
        self.calories = item[4] 
        self.total_fat = item[5] [:-2]
        self.saturated_fat = item[6] [:-2]
        self.polyunsaturated_fat = item[7] [:-2]
        self.monounsaturated_fat = item[8] [:-2]
        self.cholesterol = item[9] [:-2]
        self.sodium = item[10][:-2] 
        self.potassium = item[11][:-2] 
        self.total_carbohydrate = item[12][:-2] 
        self.dietary_fiber = item[13][:-2] 
        self.sugars = item[14][:-2] 
        self.protein = item[15][:-2] 
        self.vitamin_a = item[16][:-2] 
        self.vitamin_b12 = item[17][:-2] 
        self.vitamin_b6 = item[18][:-2] 
        self.vitamin_c = item[19][:-2] 
        self.vitamin_d = item[20][:-2] 
        self.vitamin_e = item[21][:-2] 
        self.calcium = item[22][:-2] 
        self.copper = item[23][:-2] 
        self.folate = item[24][:-2] 
        self.iron = item[25][:-2] 
        self.magnesium = item[26][:-2] 
        self.manganese = item[27][:-2] 
        self.niacin = item[28][:-2] 
        self.pantothenic_acid = item[29][:-2] 
        self.phosphorus = item[30][:-2] 
        self.riboflavin = item[31][:-2] 
        self.selenium = item[32][:-2] 
        self.thiamin = item[33][:-2] 
        self.zinc = item[34][:-2] 

    def __str__(self):
        return self.food
