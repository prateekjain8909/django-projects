import mysql.connector
from mysql.connector import Error
from scrapping import nutrition_value
import sqlite3
from ingredients import ingredients
from scrapping import food
from procedure import procedure
\
# connection_to_nutrition=sqlite3.connect("food_nutrition (copy)")
# cursor_to_nutrition = connection_to_nutrition.cursor()
# insert_nutrition = """INSERT INTO Vegeterian (Food ,Servings_Per_Recipe, Serving_Size, Calories , Total_Fat  , Saturated_Fat  , Polyunsaturated_Fat  , Monounsaturated_Fat  , Cholesterol  , Sodium  , Potassium  , Total_Carbohydrate  , Dietary_Fiber  , Sugars  , Protein  , Vitamin_A  , Vitamin_B12  , Vitamin_B6  , Vitamin_C  , Vitamin_D  , Vitamin_E  , Calcium  , Copper  , Folate  , Iron  , Magnesium  , Manganese  , Niacin  , Pantothenic_Acid  , Phosphorus  , Riboflavin  , Selenium  , Thiamin  , Zinc ) 
#                         VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}","{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}") """.format("Dahi","1","1",str(nutrition_value[1]),str(nutrition_value[2]),str(nutrition_value[3]),str(nutrition_value[4]),str(nutrition_value[5]),str(nutrition_value[6]),str(nutrition_value[7]),str(nutrition_value[8]),str(nutrition_value[9]),str(nutrition_value[10]),str(nutrition_value[11]),str(nutrition_value[12]),str(nutrition_value[13]),str(nutrition_value[14]),str(nutrition_value[15]),str(nutrition_value[16]),str(nutrition_value[17]),str(nutrition_value[18]),str(nutrition_value[19]),str(nutrition_value[20]),str(nutrition_value[21]),str(nutrition_value[22]),str(nutrition_value[23]),str(nutrition_value[24]),str(nutrition_value[25]),str(nutrition_value[26]),str(nutrition_value[27]),str(nutrition_value[28]),str(nutrition_value[29]),str(nutrition_value[30]),str(nutrition_value[31]))

# cursor_to_nutrition.execute(insert_nutrition)
# connection_to_nutrition.commit()
# cursor_to_nutrition.close()
# connection_to_nutrition.close()


connection_to_recipie=sqlite3.connect("food_nutrition (copy)")
cursor_to_recipie = connection_to_recipie.cursor()
insert_recipie = """ INSERT INTO Recipie (Food,Ingredients,Procedure)
            VALUES("{}", "{}", "{}") """.format(food,ingredients,procedure)
cursor_to_recipie.execute(insert_recipie)
connection_to_recipie.commit()
cursor_to_recipie.close()
connection_to_recipie.close()
