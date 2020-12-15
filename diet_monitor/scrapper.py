from bs4 import BeautifulSoup as bs
import urllib.request
# from selenium import webdriver
from bs4 import BeautifulSoup as bs
import urllib.request
import re
import sqlite3

# url = "https://recipes.sparkpeople.com/recipe-detail.asp?recipe=18160"
# html = urllib.request.urlopen(url).read()
# soup = bs(html, "html.parser")

def get_ingredients(soup):
    ingredients = soup.find(id="ingredients").get_text("\n").strip()
    return ingredients
    
def get_procedure(soup):
    procedure = soup.find(id="directions_w").get_text().strip()
    return procedure

def get_food_name(soup):
    name = soup("h1")[0].get_text().strip()
    return name

def get_servings(soup):
    no_of_servings = soup.find(itemprop="recipeYield").get_text().strip()
    return no_of_servings

def get_info_url(soup):
    ing_info = soup.find(id="ingred_info")
    href = ing_info.a["href"]
    return "https://recipes.sparkpeople.com/" + href

def get_nut_value(url):
    nutrition_value=[]
    html = urllib.request.urlopen(url).read()
    soup = bs(html, "html.parser")
    tds = soup("td")
    n=0
    for td in tds:
        nutrition_value.append(td.get_text().strip())
        n += 1
        if n == 31:
            break
    return nutrition_value
# print(get_ingredients(soup))
# print(get_nut_value(get_info_url(soup)))
# browser = webdriver.Chrome()
# br = browser.get(get_info_url(soup))

# from full_data import get_ingredients,get_food_name,get_info_url,get_nut_value,get_procedure,get_servings
url = "https://recipes.sparkpeople.com/browse-results.asp?category=indian&sort=newest&pagenum=1"
 
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
 
list_of_food = get_list_of_food(url)
 
database="Food_Nutrition.db"
 
connection_to_nutrition=sqlite3.connect(database)
cursor_to_nutrition = connection_to_nutrition.cursor()
create_nutrition = """CREATE TABLE "Vegeterian" ( `Food` TEXT NOT NULL, `Calories` TEXT, `Total_Fat` TEXT, `Saturated_Fat` TEXT, `Polyunsaturated_Fat` TEXT, `Monounsaturated_Fat` TEXT, `Cholesterol` TEXT, `Sodium` TEXT, `Potassium` TEXT, `Total_Carbohydrate` TEXT, `Dietary_Fiber` TEXT, `Sugars` TEXT, `Protein` TEXT, `Vitamin_A` TEXT, `Vitamin_B12` TEXT, `Vitamin_B6` TEXT, `Vitamin_C` TEXT, `Vitamin_D` TEXT, `Vitamin_E` TEXT, `Calcium` TEXT, `Copper` TEXT, `Folate` TEXT, `Iron` TEXT, `Magnesium` TEXT, `Manganese` TEXT, `Niacin` TEXT, `Pantothenic_Acid` TEXT, `Phosphorus` TEXT, `Riboflavin` TEXT, `Selenium` TEXT, `Thiamin` TEXT, `Zinc` TEXT )"""
cursor_to_nutrition.execute(create_nutrition)
 
connection_to_recipie=sqlite3.connect(database)
cursor_to_recipie = connection_to_recipie.cursor()
create_recipie = 'CREATE TABLE "Recipie" ( `Food` TEXT, `Servings` TEXT, `Ingredients` TEXT, `Procedure` TEXT )'
cursor_to_recipie.execute(create_recipie)
 
for food in list_of_food:
    page = "https://recipes.sparkpeople.com/" + food
    html = urllib.request.urlopen(page).read()
    soup = bs(html, "html.parser")
    food_name = get_food_name(soup)
    ingredients = get_ingredients(soup)
    procedure = get_procedure(soup)
    servings = get_servings(soup)
    url = get_info_url(soup)
    nutrition_value = get_nut_value(url)
    insert_nutrition = """INSERT INTO Vegeterian (Food , Calories , Total_Fat  , Saturated_Fat  , Polyunsaturated_Fat  , Monounsaturated_Fat  , Cholesterol  , Sodium  , Potassium  , Total_Carbohydrate  , Dietary_Fiber  , Sugars  , Protein  , Vitamin_A  , Vitamin_B12  , Vitamin_B6  , Vitamin_C  , Vitamin_D  , Vitamin_E  , Calcium  , Copper  , Folate  , Iron  , Magnesium  , Manganese  , Niacin  , Pantothenic_Acid  , Phosphorus  , Riboflavin  , Selenium  , Thiamin  , Zinc ) 
                        VALUES("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}","{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}") """.format(food_name,str(nutrition_value[0]),str(nutrition_value[1]),str(nutrition_value[2]),str(nutrition_value[3]),str(nutrition_value[4]),str(nutrition_value[5]),str(nutrition_value[6]),str(nutrition_value[7]),str(nutrition_value[8]),str(nutrition_value[9]),str(nutrition_value[10]),str(nutrition_value[11]),str(nutrition_value[12]),str(nutrition_value[13]),str(nutrition_value[14]),str(nutrition_value[15]),str(nutrition_value[16]),str(nutrition_value[17]),str(nutrition_value[18]),str(nutrition_value[19]),str(nutrition_value[20]),str(nutrition_value[21]),str(nutrition_value[22]),str(nutrition_value[23]),str(nutrition_value[24]),str(nutrition_value[25]),str(nutrition_value[26]),str(nutrition_value[27]),str(nutrition_value[28]),str(nutrition_value[29]),str(nutrition_value[30]))
 
    insert_recipie = """ INSERT INTO Recipie (Food,Servings,Ingredients,Procedure)
            VALUES("{}", "{}", "{}","{}") """.format(food_name,servings, ingredients,procedure)
    cursor_to_recipie.execute(insert_recipie)
    
 
    cursor_to_nutrition.execute(insert_nutrition)
    
    print("successful")
connection_to_recipie.commit()
connection_to_nutrition.commit()
cursor_to_recipie.close()
connection_to_recipie.close()
cursor_to_nutrition.close()
connection_to_nutrition.close()