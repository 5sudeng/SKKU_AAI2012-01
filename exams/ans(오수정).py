# 컴퓨팅사고및응용(1분반)

# 학번: 2021313031
# 이름: 오수정
# 휴대폰 번호: 01096912347
# 시험 장소: 집


# 1
print("------- 1 -------")
# 함수 fun(n)은 분을 매개변수 n으로 받아 시분로 변환하여 직접 출력한다.
# 주석처럼 결과가 출력되도록 '''''' 위치에 반복문을 사용하여 이 함수를 완성하시오.
# 단, 나눗셈 및 나머지 연산(함수 포함)을 사용할 수 없다. (사용하면 0점).


def fun(n):
    ''''''
    h = 0
    m = 0
    while n >= 60 :
        n -= 60
        h += 1
    m = n
    
    print(f"{h}:{m:02d}")



fun(60)	    	# 1:00
fun(1439)	# 23:59
fun(0)		# 0:00




# 2
print("------- 2 -------")
# 함수 fun(n)은 음이 아닌 정수 n의 값을 천 단위 마다 콤마를 넣고
# 맨 왼쪽에는 $가 있는 문자열을 반환한다.
# 주석처럼 결과가 출력되도록 '''''' 위치에 이 함수를 완성하시오.  

def fun(n):
    ''''''
    if n < 0 :
        return "음이 아닌 정수를 입력하세요."
    n = list(str(n))
    for i in range(len(n)//3):
        cnt = -3*(i+1)-i
        if cnt == -1*len(n) :
            continue
        n.insert(-3*(i+1)-i,",")
    return "$"+"".join(n) 
    

print(fun(0))       # $0
print(fun(1000))    # $1,000
print(fun(123))     # $123
print(fun(123456))  # $123,456



# 3
print("------- 3 -------")
# n이 양의 홀수일 때, 함수 fun(n)이 반환하는 문자열을 출력하면 맨 아래에 있는
#  *가 n개인 피라미드 모양이 된다. '''''' 위치에 일반성 있게 이 함수를 완성하시오.

def fun(n):
    ''''''
    star = ""
    for i in range(1, n//2+1 +1) :
        star += " "*(n//2-i+1) + "*"*(i*2-1)
        star += "\n"
    return star

print(fun(1))       # *

print(fun(5))       #   *
                    #  ***
                    # *****
                    
print(fun(7))       #    *
                    #   ***
                    #  *****
                    # *******




# 4
print("------- 4 -------")
# 함수 fun(a, b)는 양의 정수 a와 정수 b사이에 있는 3의 배수의 합을 반환한다.
# 주석처럼 결과가 출력되도록 '''''' 위치에 함수 fun(a, b)를 완성하시오.

def fun(a,b):
    start = stop = step = sum = 1
    ''''''
    start = a
    stop = b + 1
    step = 3
    sum = 0
    
    while start % 3 != 0 :
        start += 1
   
    for n in range(start, stop, step):
        sum += n

    return sum

print(fun(3,6))     # 9
print(fun(1,6))     # 9
print(fun(1,2))     # 0
print(fun(6,3))     # 0
print(fun(2,15))    # 45
print(fun(2,16))    # 45
print(fun(2,17))    # 45





# 5
print("------- 5 -------")
# 함수 fun(s)는 문자열 s에 있는 각 문자 뒤에 점을 추가하여 반환한다.
# 주석처럼 결과가 나오도록 '''''' 위치에 이 함수를 완성하시오.

def fun(s):
    ''''''
    return ".".join(s)+"."
    
print(fun("hello"))     # h.e.l.l.o.
print(fun("world"))     # w.o.r.l.d.




# 6
print("------- 6 -------")
# 함수 fun1()은 −100~100인 정수 10개를 랜덤하게 생성한 리스트를 반환한다.
# 참조로 램덤하기 때문에 주석과 다른 결과가 나올 수 있다. 
# 함수 fun2(list)는 짝수인 list의 원소의 절대값으로 만든 리스트를 반환한다.
# 이 두함수를 리스트 함축(list comprehension)을 사용하여 '''''' 위치에
# 일반성 있게 작성하시오. 단, 함수 abs는 사용 금지.

''''''
import random
def fun1():
    ''''''
    return random.sample(range(-100,100),10)

def fun2(list):
    ''''''
    return [x if x > 0 else -1*x for x in list if x%2==0]
list = fun1()
print(list)         # [-100, 100, -2, 3, 4, 7, 33, 44,-21, -22]
print(fun2(list))   # [100, 100, 2, 4, 44, 22]




# 7
print("------- 7 -------")
# 함수 fun(n)은 음이 아닌 정수 n을 2진수 문자열로 변환하며,
# 이 문자열의 길이와 문자열을 반환한다.
# 주석처럼 결과가 나오도록 '''''' 위치에 이 함수를 완성하시오.

def fun(n):
    ''''''
    isZero = True
    num = n
    cnt = 1
    bin = ""
    while  num >= 1:
        bin = str(num % 2) + bin
        num //= 2
        isZero = False
    if isZero == True :
        bin = "0"
    return len(bin), bin

print(fun(0))       # (1, '0')
print(fun(1))       # (1, '1')
print(fun(23))      # (5, '10111')
print(fun(1234))    # (11, '10011010010')





# 다음 1줄은 답안을 작성하기 전에 발생하는 오류를 방지하기 위해 있음.
def Rect(a, b): pass


# 8
print("------- 8 -------")
# 주석처럼 결과가 나오도록 '''''' 위치에 클래스 Rect (직사각형)를 작성하시오.
# 객체는 가로(width)와 세로(height)로 파라메러로  생성한다.
# 객체 a을 print 하면 a의 width와 height가 출력된다. 
# 두 객체 a, b의 면적(width * height)이 같을 때 a == b가 True가 된다.

''''''
class Rect() :
    def __init__(self, w, h) :
        self.width = w
        self.height = h

    def setWidth(self, width) :
        self.width = width

    def setHeight(self, height) :
        self.height = height

    def getWidth(self) :
        return self.width

    def getHeight(self) :
        return self.height
    
    def __str__(self) :
        return f"width = {self.width}, height = {self.height}"
    
    def __eq__(self, other) :
        return self.width*self.height == other.width*other.height


a = Rect(3.0, 5.0)  # width가 3이고 height가 5인 객체 생성
b = Rect(7.5, 2.0)
c = Rect(3.0, 4.0)

print(a)            # width = 3.0, height = 5.0
print(c)            # width = 3.0, height = 4.0
print(a == b)       # True
print(b == c)       # False


# In[ ]:




