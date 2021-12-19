def function_tips():
    '''功能：每天输出一条励志文字'''
    import datetime
    #定义一个列表
    mot=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    day=datetime.datetime.now().weekday()#获取当前星期
    print(mot[day])

function_tips()