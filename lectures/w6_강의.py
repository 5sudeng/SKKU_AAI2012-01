print("\n제8장 객체와 클래스\n")

print("#P.7")
print("Everything in Python is an object".upper())

print("\n#P.13")
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):self.count += 1
a = Counter()
a.increment()
print("카운터의값=", a.count)

print("\n#P.14")
class Counter:
    def __init__(self) :
        self.count= 0
    def increment(self):
        self.count+= 1
c = Counter()

class Counter:
    def __init__(self,  initValue=0) :
        self.count= initValue
    def increment(self):
        self.count+= 1
a = Counter(100)
b = Counter()

print("\n#P.17")
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
    def show(self):
        print(self.channel, self.volume, self.on)
    def setChannel(self, channel):
        self.channel = channel
    def getChannel(self):
        return self.channel
t = Television(9, 10, True)
t.show()
t.setChannel(11)
t.show()

print("\n#P.18")
import math 
class Circle:
    def __init__(self, radius = 0):
        self.radius= radius
    def getArea(self):
        return  math.pi* self.radius* self.radius
    def getPerimeter(self):
        return 2 * math.pi* self.radius# Circle 객체를생성한다. 
c = Circle(10)
print("원의면적", c.getArea())
print("원의둘레", c.getPerimeter())

print("\n#P.20")
class Car:
    def __init__(self, speed, color, model):
        self.speed= speed
        self.color= color
        self.model= model
    def drive(self):
        self.speed= 60
myCar= Car(0, "blue", "E-class")
print("자동차객체를생성하였습니다.")
print("자동차의속도는", myCar.speed)
print("자동차의색상은", myCar.color)
print("자동차의모델은", myCar.model)
myCar.drive()
print("자동차의속도는", myCar.speed)

print("\n#P.23")
class Student:
    def __init__(self, name=None, age=0):
        self.__name= name
        self.__age= age
    def getAge(self):
        return self.__age
    def getName(self):
        return self.__name
    def setAge(self, age):
        self.__age=age
    def setName(self, name):
        self.__name=name
obj=Student("Hong", 20)
obj.getName()

print("\n#P.25")
class BankAccount:
    def __init__(self):
        self.__balance= 0
    def withdraw(self, amount):
        self.__balance-= amount
        print("통장에서", amount, "가 출금되었음")
        return self.__balance
    def deposit(self, amount):
        self.__balance+= amount
        print("통장에", amount, "가 입금되었음")
        return self.__balance
a = BankAccount()
a.deposit(100)
a.withdraw(10)


print("\n#P.29")
myTV = None
if myTV is None :
    print("현재 TV가 없습니다.")


print("\n#P.30,33")
class Television :
    serialNumber = 0
    def __init__(self, channel, volume, on) :
        self.channel = channel
        self.volume = volume
        self.on = on
        Television.serialNumber += 1
        self.number = Television.serialNumber
    
    def show(self) :
        print(self.channel,self.volume,self.on,self.serialNumber)

def setSilentMode(t) :
    t.volume = 2

myTV = Television(11,10,True)
setSilentMode(myTV)
myTV.show()


print("\n#P.34")
class Monster :
    WEAK = 0
    NORMAL = 10
    STRONG = 20
    VERY_STRONG = 30

    def __init__(self) :
        self.__health = Monster.NORMAL
    def eat(self) :
        self.__health = Monster.STRONG
    def attack(self) :
        self.__health = Monster.WEAK

print("\n#P.35")
class Dog :
    kind = "bulldog"
    def __init__(self, name, age) :
        self.name = name
        self.age = age

print("\n#P.39")
class Vector2D :
    def __init__(self, x, y) :
        self.x = x
        self.y = y
    def __add__(self, other) :
        return Vector2D(self.x + other.x, self.y + other.y)
    def __sub__(self, other) :
        return Vector2D(self.x - other.x, self.y - other.y)
    def __eq__(self, other) :
        return self.x == other.x and self.y == other.y
    def __str__(self) :
        return f"({self.x},{self.y})"
    
u = Vector2D(0,1)
v = Vector2D(1,0)
w = Vector2D(1,1)
a = u + v
print(a)
print(a == w)

print("\n#P.40")
from random import randint
class Dice :
    def __init__(self, x, y) :
        self.__x = x
        self.__y = y
        self.__size = 30
        self.__value = 1
    def read_dice(self) :
        return self.__value
    def print_dice(self) :
        print("주사위의 값 =",self.__value)
    def roll_dice(self) :
        self.__value = randint(1,6)
d = Dice(100,100) 
d.roll_dice()
d.print_dice()
