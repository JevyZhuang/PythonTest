def fun_checkout(money):
    '''功能：计算商品合计金额并进行折扣处理
    money：保存商品金额的列表
    返回商品的合计金额和折扣后的金额'''
    money_old=sum(money)
    money_now=money_old
    if 500<=money_old<1000:
        money_now='{:.2f}'.format(money_old*0.9)
    elif 1000<=money_old<2000:
        money_now='{:.2f}'.format(money_old*0.8)
    elif 2000<=money_old<3000:
        money_now='{:.2f}'.format(money_old*0.7)
    elif 3000>=money_old:
        money_now='{:.2f}'.format(money_old*0.6)
    return money_old,money_now

list_money=[]
while True:
    inmoney=float(input("输入商品金额（输入0表示输入完毕）："))
    if int(inmoney)==0:
        break
    else:
        list_money.append(inmoney)
money =fun_checkout(list_money)
print("合计金额：",money[0],"应付金额：",money[1])