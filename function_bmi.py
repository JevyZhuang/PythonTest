def function_bmi(person,height,weight):
    '''功能：根据身高和体重计算BMI指数
    person：姓名
    height：身高，单位：米
    weight：体重，单位：千克'''
    print(person+"的身高："+str(height)+"米 \t 体重："+str(weight)+"千克")
    bmi=weight/(height*height)
    print(person+"的BMI指数为："+str(bmi))
    #判断身材是否合理
    if bmi<18.5:
        print("过轻")
    if bmi>=18.5 and bmi<24.9:
        print("正常")
    if bmi>=24.9 and bmi<29.9:
        print("过重")
    if bmi>=29.9:
        print("肥胖")

function_bmi("甲",1.83,60)
function_bmi("乙",1.60,50)
function_bmi("丙",1.76,75)