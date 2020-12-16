from bs4 import BeautifulSoup as bs
import urllib.request

url = "https://recipes.sparkpeople.com/recipe-detail.asp?recipe=18160"
html = urllib.request.urlopen(url).read()
soup = bs(html, "html.parser")

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