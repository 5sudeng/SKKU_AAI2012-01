print("\n#1")
class Rectangle() :
    def __init__(self, x, y, w, h) :
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def setX(self, x) :
        self.x = x
    def setY(self, y) :
        self.y = y
    def setWidth(self, width) :
        self.width = width
    def setHeight(self, height) :
        self.height = height
    def getX(self) :
        return self.x
    def getY(self) :
        return self.y
    def getWidth(self) :
        return self.width
    def getHeight(self) :
        return self.height

    def Overlap(self, r) :
        if (self.x - self.width > r.x + r.width) or (self.x + self.width < r.x - r.width) or (self.y + self.height < r.y - r.height) or (self.y - self.height > r.y + r.height) :
            print(f"{self}와 {r}은 서로 겹치지 않습니다.")
        else :
            print(f"{self}와 {r}은 서로 겹칩니다.")
    
    def getArea(self) :
        return self.width*self.height

    def __str__(self) :
        return f"({self.x},{self.y},{self.width},{self.height})"

r1 = Rectangle(0,0,100,100)
r2 = Rectangle(10,10,100,100)
r1.Overlap(r2)

print("\n#2")    
class PhoneBook():
    def __init__(self) :
        self.contact = {}
    def __str__(self) :
        s = ""
        for i in sorted(self.contact) :
            s += str(self.contact[i][0]) + "\n" + "office phone: " + str(self.contact[i][2])+ "\n" +"email address: "+str(self.contact[i][3])+'\n\n'
        return s
    def add(self, name, mobile = None, office = None, email = None) :
        self.contact[name] = [name, mobile, office, email]
#if 세번! None 이 아닐때마다 추가하기. items로 가져오기?
obj = PhoneBook()
obj.add("Kim",office = "1234567", email = "kim@company.com")
obj.add("Park",office = "2345678",email = "park@company.com")
print(obj)