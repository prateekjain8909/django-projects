from bs4 import BeautifulSoup as bs
import urllib.request
import re
from full_data import get_ingredients,get_food_name,get_info_url,get_nut_value,get_procedure,get_servings
import csv

def get_list_of_food(page_url):
    html = urllib.request.urlopen(page_url).read()
    soup = bs(html, "html.parser")
    results = soup.find(id="res11_w")
    href = results.find_all(href=re.compile("recipe-detail.asp?"))
    n = -1
    urls=[]
    for i in href:
        n+=1
        if n % 3 != 0:
            continue
        i=i["href"]
        urls.append(i)
    return urls

def data_entry(food,writer_handler):
    page = "https://recipes.sparkpeople.com/" + food
    html = urllib.request.urlopen(page).read()
    soup = bs(html, "html.parser")
    food_name = get_food_name(soup)
    ingredients = get_ingredients(soup)
    procedure = get_procedure(soup)
    servings = get_servings(soup)
    url = get_info_url(soup)
    nutrition_value = get_nut_value(url)
    nutrition_value.insert(0, food_name)
    writer_handler.writerow(nutrition_value)

    # insert_recipie = """ INSERT INTO Recipie (Food,Servings,Ingredients,Procedure)
    #         VALUES("{}", "{}", "{}", "{}") """.format(str(food_name),str(servings), str(ingredients),str(procedure))   
    print("successful")
    return

temp = "https://recipes.sparkpeople.com/browse-results.asp?category=indian&sort=newest&pagenum="
database = "food_nutrition.csv"
column_header = ["Food"  , "Calories"  , "Total Fat"  , "Saturated Fat"  , "Polyunsaturated Fat"  , "Monounsaturated Fat"  , "Cholesterol"  , "Sodium"  , "Potassium"  , "Total Carbohydrate"  , "Dietary Fiber"  , "Sugars"  , "Protein"  , "Vitamin A"  , "Vitamin B-12"  , "Vitamin B-6"  , "Vitamin C"  , "Vitamin D"  , "Vitamin E"  , "Calcium"  , "Copper"  , "Folate"  , "Iron"  , "Magnesium"  , "Manganese"  , "Niacin"  , "Pantothenic Acid"  , "Phosphorus"  , "Riboflavin"  , "Selenium"  , "Thiamin"  , "Zinc"]
data = open(database, "w")
writer_handler = csv.writer(data)
writer_handler.writerow(column_header)
    

for i in range(1, 2):
    url= temp + str(i)
    list_of_food = get_list_of_food(url)
    for food in list_of_food:
        data_entry(food,writer_handler)
