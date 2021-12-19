class Geese:
    '''大雁类'''
    def __init__(self,beak,wing,claw):
        print("大雁类")
        print(beak)
        print(wing)
        print(claw)
    def fly(self,state):
        print(state)

beak_1="鸟嘴"
wing_1="翅膀"
claw_1="爪子"
wildGoose=Geese(beak_1,wing_1,claw_1)
wildGoose.fly("飞")