import sqlite3
import csv
file_name = "food_nutrition.csv"
connection = sqlite3.connect("Food Nutrition.db")
cursor = connection.cursor()

with open(file_name, "r") as f:
    csv_reader = csv.reader(f)
    # column_header = next(csv_reader)
    # column_header1 = next(csv_reader)
    n=0
    for food in csv_reader:
        recipie = [0]
        recipie[0] = food[0]
        recipie.append(food.pop(1))
        recipie.append(food.pop(1))
        recipie.append(food.pop(1))
        n+=1
        try:
            insert_nutrition = """INSERT INTO Nutrition (Food , Calories , Total_Fat  , Saturated_Fat  , Polyunsaturated_Fat  , Monounsaturated_Fat  , Cholesterol  , Sodium  , Potassium  , Total_Carbohydrate  , Dietary_Fiber  , Sugars  , Protein  , Vitamin_A  , Vitamin_B12  , Vitamin_B6  , Vitamin_C  , Vitamin_D  , Vitamin_E  , Calcium  , Copper  , Folate  , Iron  , Magnesium  , Manganese  , Niacin  , Pantothenic_Acid  , Phosphorus  , Riboflavin  , Selenium  , Thiamin  , Zinc ) 
                                VALUES(?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
                                
            cursor.execute(insert_nutrition, tuple(food))
            insert_recipie = """ INSERT INTO Recipie (Food,Ingredients,Procedure,Servings)
                VALUES(?, ?, ?, ?) """
            cursor.execute(insert_recipie,tuple(recipie))  
            connection.commit()
        except Exception:
            print(n)
            break
cursor.close()
connection.close()

# create = 'CREATE TABLE "customers" ( `name` TEXT, `address` TEXT)'
# cursor.execute(create)
# sql = "INSERT INTO customers (name, address) VALUES (?, ?)"
# val = ('Peter', 'Lowstreet 4')
# #   ('Amy', 'Apple st 652'),
# #   ('Hannah', 'Mountain 21'),
# #   ('Mich"ael', 'Valley 345'),
# #   ('Sandy', 'Ocean blvd 2'),
# #   ('Betty', 'Green Grass 1'),
# #   ('Richard', 'Sky st 331'),
# #   ('Susan', 'One way "98'),
# #   ('Vicky', 'Yellow Garden 2'),
# #   ('Ben', 'Park Lane 38'),
# #   ('William', 'Central st 954'),
# #   ('Chuck', 'Main Road 989'),
# #   ('Viola', 'Sideway 1633')
# # ]

# cursor.execute(sql, val)

