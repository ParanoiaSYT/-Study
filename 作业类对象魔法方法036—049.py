# 036
# 人名类
class Person():
    def setName(self, name='小甲鱼'):
        self.name = name
        print(self.name)

a = Person()
a.setName()
a.setName('王多余')

# 矩形类
# class Rectangle:
#     length = 5
#     width = 4
#
#     def setRect(self):
#         print('请输入矩形的长和宽...')
#         self.length = float(input('长：'))
#         self.width = float(input('宽：'))
#
#     def getRect(self):
#         print('矩形的长和宽分别为:%.2f和%.2f' % (self.length, self.width))
#
#     def getArea(self):
#         S = self.length * self.width
#         print('矩形的面积为：%d' % S)
#
# b = Rectangle()
# b.setRect()
# b.getRect()
# b.getArea()

# 037
class MyClass:
    name = 'FishC'

    def myFun(self):
        print("Hello FishC!")

print(MyClass.name)
a=MyClass()
a.myFun()

#游乐园票价
# class Ticket():
#     def __init__(self,weekend=False):
#         price = float(input('平日票价为：'))
#         if weekend:
#             self.price=price*1.2
#         else:
#             self.price=price
#     def all_price(self,adult=1,child=0):
#         adult=int(input('请输入成年人数量：'))
#         child=int(input('请输入儿童数量：'))
#         cost=adult*self.price+child*self.price/2
#         print('%d个成年人和%d个儿童共需%.2f元'%(adult,child,cost))
# a=Ticket(weekend=1)
# a.all_price()

#乌龟吃鱼
import random as r
legal_x=[0,10]
legal_y=[0,10]

class Gui():            #乌龟的操作有：能量变化，移动，吃鱼
    def __init__(self):
        self.power=100
        self.x=r.randint(legal_x[0],legal_x[1])
        self.y=r.randint(legal_y[0],legal_y[1])
        speed=int(input('乌龟每次移动的步伐为speed='))
    def move(self,speed=1):
        new_x=self.x+r.choice([speed,-speed])
        new_y=self.y+r.choice([speed,-speed])

        if new_x<legal_x[0]:
            self.x=legal_x[0]-(new_x-legal_x[0])
        elif new_x>legal_x[1]:
            self.x=legal_x[1]+(legal_x[1]-new_x)
        else:
            self.x=new_x

        if new_y<legal_y[0]:
            self.y=legal_y[0]-(new_y-legal_y[0])
        elif new_y>legal_y[1]:
            self.y=legal_y[1]+(legal_y[1]-new_y)
        else:
            self.y=new_y

        self.power-=1
        return (self.x,self.y)

    def eat(self):
        self.power+=20
        if self.power>100:
            self.power=100

class Fish():
    def __init__(self):
        self.x=r.randint(legal_x[0],legal_x[1])
        self.y=r.randint(legal_y[0],legal_y[1])
    def move(self):
        new_x=self.x+r.choice([1,-1])
        new_y=self.y+r.choice([1,-1])

        if new_x < legal_x[0]:
            self.x = legal_x[0] - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            self.x = legal_x[1] + (legal_x[1] - new_x)
        else:
            self.x = new_x

        if new_y < legal_y[0]:
            self.y = legal_y[0] - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            self.y = legal_y[1] + (legal_y[1] - new_y)
        else:
            self.y = new_y

        return (self.x,self.y)

# class Goldfish(Fish):
#     pass
# class Carp(Fish):
#     pass
# class Salmon(Fish):
#     pass
# class Shark(Fish):
#     def __init__(self):       #子类重写了父类的方法就会覆盖
#         # Fish.__init__(self)         #未绑定的父类，给的是子类的实例对象
#         super(Shark, self).__init__()      #或者用super函数方法（不用给出继类名字）
#         self.hungry=True
#     def eat(self):
#         if self.hungry==True:
#             print('吃吃吃吃吃次吃吃吃')
#             self.hungry=False
#         else:
#             print('吃饱了')
# shark=Shark()
# shark.eat()

gui=Gui()
fish=[]     #鱼群列表
for i in range(10):
    new_fish=Fish()
    fish.append(new_fish)

while True:
    if not len(fish):
        print('鱼🐟都被吃完啦！')
        break
    elif not gui.power:
        print('乌龟的能量耗完啦')
        break

    pos=gui.move()

    # 在迭代器中删除列表元素是非常危险的，经常会出现意想不到的问题，因为迭代器是直接引用列表的数据进行引用
    # 这里我们把列表拷贝给迭代器，然后对原列表进行删除操作就不会有问题了^_^
    for each_fish in fish.copy():
        if each_fish.move()==pos:
            gui.eat()
            fish.remove(each_fish)
            print('一条鱼🐟被吃掉啦！')



