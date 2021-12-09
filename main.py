# -*- coding:utf-8 -*-
'''
@功能：根据身高，体重计算BMI指数
@author：无语
@create：2021-12-9
'''
# 程序开始
# 输入身高和体重
height=float(input("请输入您的身高："))
weight=float(input("请输入您的体重："))
bmi=weight/(height*height)
print("您的BMI指数为："+str(bmi))

#判断身材是否合理
if bmi<18.5:
    print("您的体重过轻")
if bmi>=18.5 and bmi<24.9:
    print("正常范围，请继续保持")
if bmi>=24.9 and bmi<29.9:
    print("您的体重过胖")
if bmi>=29.9:
    print("肥胖")
#程序结束