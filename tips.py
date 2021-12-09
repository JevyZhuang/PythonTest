import datetime
#定义一个列表
mot=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
day=datetime.datetime.now().weekday()
print(mot[day])