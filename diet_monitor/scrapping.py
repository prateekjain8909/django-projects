import selenium
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import mysql.connector
import urllib.request
import re
url = "https://recipes.sparkpeople.com/recipe-calories.asp?recipe=18160"
# browser = webdriver.Chrome()
# br = browser.get(url)
html = urllib.request.urlopen(url).read()
soup = bs(html, "html.parser")
tds = soup("td")
h1 = soup("h1")
nutrition_type = []
nutrition_value=[]
nutrition_value1=[]
food = re.findall(".+>(.+)<", str(h1))[0]
import time

# start=time.time()
for td in tds:
    nutrition_value1.append(td.get_text().strip())
# print(nutrition_value1)
# end = time.time()
# print(end-start)
# ths = soup("th")
# for th in ths:
#     nutrition_type.append(str(re.findall('.+>(.+)<', str(th))[0]))
# with open("new.txt", "w") as f:
#     f.write(str(food)+"\n\n")
#     for i in range(len(nutrition_type)):
#         f.write(str(nutrition_type[i])+"      "+ str(nutrition_value[i])+"\n")
nutrition_value.insert(0, food)
# print(type(nutrition_value[31]))