def division():
    '''功能：分苹果'''
    apple=int(input("请输入苹果的个数："))
    children=int(input("请输入来了几个小朋友："))
    result=apple//children
    remain=apple-result*children
    if remain>0:
        print(apple,"个苹果，平均分给",children,"个小朋友，每个人分",result,"个，剩下",remain,"个")
    else:
        print(apple,"个苹果，平均分给",children,"个小朋友，每个人分",result,"个")
if __name__=='__main__':
    try:
        division()
    except ZeroDivisionError:
        print("\n出错了，苹果不能被0个小朋友分！")