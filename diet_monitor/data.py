import selenium
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import mysql.connector

import urllib.request
import re, csv
import sqlite3
url = "https://medicine.careers360.com/articles/neet-cutoff-up"

html = urllib.request.urlopen(url).read()
soup = bs(html, "html.parser")
results = soup.find(id="res11_w")
href = results.find_all(href=re.compile("recipe-detail.asp?"))

connection = sqlite3.connect("data.db")
cursor = connection.cursor()
html = urllib.request.urlopen(url).read()
soup = bs(html, "html.parser")
tables = soup("tbody")
c=0
for table in tables:
    # print(table)
    trs = soup("tr")
    for tr in trs:
        # print(tr)
        college=[]
        for t in tr:
            try:
                college.append(t.get_text().strip())
            except Exception:
                print("none", end=",")
        c += 1
        
        if c < 75:
            continue
        # print(college)
        # insert = """INSERT INTO Colleges ("University","STATE","TYPE","URR","URS","OBCR","OBCS","SCR","SCS","STR","STS","EWSR","EWSS" ) 
        #                                 VALUES(?, ?, ?,?, ?, ?, ?, ?, ?,?, ?, ?, ?) """
        insert = """INSERT INTO Colleges ("University","STATE","TYPE","URR","URS","OBCR","OBCS","SCR","SCS","STR","STS") 
                                        VALUES(?, ?, ?,?, ?, ?, ?, ?, ?,?, ?) """
        # insert = """INSERT INTO Colleges ("University","STATE","TYPE","URR","URS") 
        #                                 VALUES(?, ?, ?,?, ?) """
        college.insert(1, "U.P")
        college.insert(2, "Government")
        # college.insert(2, "Private")
        # college[0]=college[0][6:]
        print(college)
        cursor.execute(insert, tuple(college))
        connection.commit()

        # print()
        # para = soup('p')
        # for i in para:
            # print(i.get_text().strip())
            # print("==================")
        
        if c==89:
            break
    # c += 1
    # if c==19:
    break
# database = "data.csv"
# column_header = ["University","URR","URS","OBCR","OBCS","SCR","SCS","STR","STS","EWSR","EWSS",]
# data = open(database, "w")
# writer_handler = csv.writer(data)
# writer_handler.writerow(column_header)
# insert = """INSERT INTO Colleges ("University","STATE","URR","URS","OBCR","OBCS","SCR","SCS","STR","STS","EWSR","EWSS", ) 
#                                 VALUES(?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) """
# cursor.execute(insert,)  
# connection.commit()

cursor.close()
connection.close()