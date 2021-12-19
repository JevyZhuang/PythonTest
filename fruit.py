class Fruit:
    color="绿色"
    def harvest(self,color):
        print("水果是",color,"色的")
        print("水果已经收获......")
        print("水果原来是：",Fruit.color,"的")
class Apple(Fruit):
    color="红色"
    def __init__(self):
        print("Apple")
class Orange(Fruit):
    color="橙色"
    def __init__(self):
        print("Orange")
apple=Apple()
apple.harvest(apple.color)
orange=Orange()
orange.harvest(orange.color)