import datetime, os
from django.core.files import File
# random_date = datetime.datetime(2020,9,11)
random_date = datetime.time(hour=14,minute=20)
# today_date = datetime.datetime.now().replace(hour=0,minute=0,microsecond=0)
today_date = datetime.datetime(2020,9,10).replace(hour=0,minute=0,microsecond=0)
# today_date=datetime.date.today()
today_time = datetime.datetime.now()
# print(today_time>today_date)
# print(random_date)
# print(today_date)
# print(today_time)
# print((today_time - today_date).days)
# datedelta = (today_time - today_date).days
# if datedelta < 1:
#     print("today")
# elif datedelta < 2:
#     print("yesterday")
# else:
#     print(random_date)
# datetime.datetime.fr
# print(datetime.datetime(2020,9,11,12,20,20))
# print("{%I}:{%M} {%p} {}/{}/{}".format(today_time))
# print(datetime.datetime.fromisoformat(today_time))
# print(datetime.datetime.now().strftime("%I:%M %p"))
save_format = datetime.datetime.now().strftime("%Y,%m,%d,%H,%M,%S")
# i = list(map(lambda x: x.lstrip('0'), save_format.split(',')))
# print(save_format)
i = list(map(int,save_format.split(',')))
# print(datetime.datetime(i[0],i[1],i[2],i[3],i[4],i[5]))
# data = [
#     {
#         "date":'2020,09,12,15,56,57',
#         "user":'user1',
#         "message":'message1'
#     },
#     {
#         "date":'2020,09,12,05,56,57',
#         "user":'user2',
#         "message":'message2'
#     },
#     {
#         "date":'2020,09,12,15,50,57',
#         "user":'user1',
#         "message":'message3'
#     },
#     {
#         "date":'2020,01,12,15,56,57',
#         "user":'user1',
#         "message":'message4'
#     },
#     {
#         "date":'2020,09,12,15,56,57',
#         "user":'user1',
#         "message":'message5'
#     },
#     {
#         "date":'2019,09,12,15,56,57',
#         "user":'user2',
#         "message":'message6'
#     },
#     {
#         "date":'2020,09,12,15,56,57',
#         "user":'user1',
#         "message":'message7'
#     },
#     {
#         "date":'2020,09,11,15,56,57',
#         "user":'user2',
#         "message":'message8'
#     },
    
# ]

# data.sort(key=lambda x:x['date'],reverse=True)
# print(data)
# for item in data:
#     i = list(map(int, item['date'].split(',')))
#     message_time = datetime.datetime(i[0], i[1], i[2], i[3], i[4], i[5])
#     today_date = datetime.datetime.now().replace(hour=0, minute=0, microsecond=0)
#     yesterday_date = today_date - datetime.timedelta(days=1)
#     if message_time>=today_date :
#         day = "today"
#         message_time_formatted = message_time.strftime("%I:%M %p "+day)
#     elif message_time>=yesterday_date :
#         day = "yesterday"
#         message_time_formatted = message_time.strftime("%I:%M %p "+day)
#     else:
#         message_time_formatted = message_time.strftime("%I:%M %p %d %b")
#     item['message_time_formatted'] = message_time_formatted
    
    
    # print(type(item))

# print(datetime.datetime.now())
def get_chat_data(message,user):
    with open('user2.py', 'r+') as f:
        myfile = File(f)
        if message:
            myfile.seek(0, 2)
            myfile.seek(myfile.tell()-1, 0)
            myfile.write('{"date1":"2020,09,12,15,56,57","user":"'+str(user)+'","message":"'+str(message)+ '"},]')
        return 
# print(type(get_chat_data("")))