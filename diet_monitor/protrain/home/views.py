from django.shortcuts import render
from .models import Nutrition
import csv
from datetime import datetime
import calendar
import re

# Create your views here.
def home(request):
    return render(request, "home/home.html")


def search(request):
    q = request.GET.get('q')
    if q:
        food = Nutrition.objects.all()
        food = re.findall(q,[str(name.food) for name in food])
        # food = NutritionDocument.search().query('match', food=q)
        print(len(q))

    else:
        food = ''
        
    return render(request, 'search.html', {'food':food})

def data(request):
    
    # with open('food_nutrition.csv', "r") as f:
    #     csv_reader = csv.reader(f)
    #     # college = list(map())
    #     n=0
    #     for item in csv_reader:
    #         n += 1
    #         food = Nutrition()
    #         try:
    #             food.fill(item)
    #             # if n % 50 == 0:
    #             print(n,"saved")
    #             # print(food)
    #             food.save()
    #         except Exception:
    #             print(n,"error")
    #         # if n==20:
    #         #     break
    return render(request,"home/1.html")

def login(request):
    return render(request, "login.html")

def monitor(request):
    # date = datetime(2019,4,14)
    date = datetime.today()
    year = date.year
    month = date.month
    # today = date.day
    # print(year, month)

  
    # text_cal = calendar.HTMLCalendar(firstweekday = 0) 
  
    cal = calendar.Calendar().itermonthdays(year, month)
    # print(type(cal))
    print(cal)
    # for day in cal:
    #     print((day))
        # break
    # printing formatmonth 
    # print(today,type(today))
    day = "{:%A}".format(date)
    month = "{:%b   %d}".format(date)
    year = "{:%B   %Y}".format(date)
    print(day)
    args = {"calendar": cal, "today": date, "day":day, "month":month, "year":year}
    # print(args['calendar'])
    return render(request, 'calendar.html',args)