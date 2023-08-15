print("\n제4장 반복문\n")

print("#P.33")
dan = int(input("원하는 단은 : "))
for i in range(1,10) :
    print("%s * %s = %s"%(dan, i, dan*i))

print()

print("#P.35")

import random
from tkinter import N

tries = 0
guess = 0 #사용자의 추측값?
answer = random.randint(1,100) #1~100사이의 난수

print("1부터 100 사이의 숫자를 맞추시오")

while guess != answer and tries < 5:
    guess = int(input("숫자를 입력하시오 : "))
    tries += 1
    if guess < answer :
        print("너무 낮음!")
    elif guess > answer :
        print("너무 높음!")

if guess == answer :
    print("축하합니다. 시도횟수 =",tries)
else :
    print("정답은",answer) #확장시를 위해  

print()

print("#P.37")

flag = True

while flag :
    x = random.randint(1,100)
    y = random.randint(1,100)
    answer = int(input(f"{x} + {y} = "))
    if answer == x + y :
        print("잘했어요!!\n")
    else :
        print("틀렸어요. 하지만 다음번에는 잘할 수 있죠?\n")
        flag = False

print("#P.39")

password = ""
while password != "pythonisfun" :
    password = input("암호를 입력하시오 : ")
print("로그인 성공\n")

print("#P.41")

for i in range(5) :
    for j in range(10) :
        print("*", end = "")
    print()

print()
print("#P.42")
for i in range(1,6) :
    for j in range(i) :
        print("*", end="")
    print()

print()
print("#P.43")
adj = ["small","medium","large"]
nouns = ["apple","banana","grape"]
for i in adj :
    for j in nouns :
        print(i, j)

print()
print("#P.44")
for i in range(1,7):
    for j in range(1,7) :
        if i + j == 6 :
            print("첫 번째 주사위 = %d 두 번째 주사위 = %d"%(i,j))

print()
print("#P.47")
while True :
    light = input("신호등 색상을 입력하시오 : ")
    if light == 'red' :
        break
print("정지!\n")

print("#P.48")
for i in range(1,11) :
    if i%3 == 0 :
        continue
    print(i, end = " ")
print()

print()
print("#P.49")

N_PRIMES = 50 
num = 2
count = 0

while count < N_PRIMES :
    divisor = 2
    prime = True
    while divisor < num :
        if num%divisor == 0 :
            prime = False 
            break
        divisor += 1
    if prime :
        count += 1
        print(num, end = " ")
    num += 1
print()

print()
print("#P.51")
divisor = 1.0 #분모
divident = 4.0 #분자
sum = 0.0
loop_cnt = int(input("반복횟수 : "))
while loop_cnt > 0 :
    sum += divident/divisor
    divisor += 2
    divident = -1.0*divident
    loop_cnt -= 1
print(f"PI = {sum}\n")

print("#P.53")
initial_money = 50
goal = 250
wins = 0

for i in range(100):
    cash = initial_money
    while cash > 0 and cash < goal :
        number = random.randint(1,2)
        if number == 1 :
            cash += 1
        else :
            cash -= 1
    if cash == goal :
        wins += 1
print("초기 금액 $%d"%initial_money)
print("목표 금액 $%d"%goal)
print("100번 중에서 %d번 성공\n"%wins)

print("\n제4장 반복문\n")

print("#P.11")
def get_area(radius) :
    if radius > 0 :
        area = 3.14*radius**2
    else :
        area = 0
    return area
result = get_area(3)
print(f"반지름이 3인 원의 면적 = {result}\n")

print("#P.13")
result1 = get_area(3)
result2 = get_area(20)
print(f"반지름이 3인 원의 면적 = {result1}")
print(f"반지름이 20인 원의 면적 = {result2}\n")

print("#P.14")
def get_input() :
    return 2,3
x, y = get_input()
print(x,y)

print("\n#P.18")
def main() :
    print("20cm 피자 2개의 면적 :",get_area(20)*2)
    print("30cm 피자 1개의 면적 :",get_area(30))
main()

print("\n#P.21")
def get_sum(start, end) :
    sum = 0 
    for i in range(start, end+1) :
        sum += i
    return sum

x = get_sum(1,10)
y = get_sum(1,20)
print(x, y)

print("\n#P.22")
def set_radius(radius) :
    radius = 100
    return radius

r = 20
set_radius(r)
print(r)

print("\n#P.22")
def greet(name, msg="별일없죠?") :
    print("안녕",name+','+msg)

greet("영희")
greet("철수", "집에가")

print("\n#P.24")
def sub(x,y,z) :
    print("x =",x,"y =",y,"z =",z)
sub(10,20,30)

print("\n#P.25")
def varfunc(*args) :
    print(args)
print("하나의 값으로 호출")
varfunc(10)
print("여러개의 값으로 호출")
varfunc(10,20,30)

print("\n#P.26")
def add(*numbers) :
    sum = 0
    for n in numbers :
        sum += n
    return sum
print(add(10,20))
print(add(10,20,30))

print("\n#P.27")
def myfunc(**kwargs):
    print(kwargs)
    result = ""
    for arg in kwargs.values():
        result += arg
    return result
print(myfunc(ace = "Hi", bee = "Mr", name = "Kim"))

print("\n#P.29")
alist = [1,2,3]
print(*alist)
print(*alist,sep=":")
print(alist)

print("\n#P.30")
def sum(a,b,c):
    print(a+b+c)
sum(*alist)

print("\n#P.31")
def display(msg, count=1) :
    for i in range(count):
        print(msg)
display("환영합니다.",5)

print("\n#P.33")
def f(x) :
    return (x**2 - x - 1)

def bisection_method(a, b, error) :
    if f(a)*f(b) > 0 :
        print("구간에서 근을 찾을 수 없습니다.")
    else :
        while (b-a)/2.0 > error :
            midpoint = (a+b)/2.0
            if f(midpoint) == 0 :
                return midpoint
            elif f(a)*f(midpoint) < 0 :
                b = midpoint
            else :
                a = midpoint
        return midpoint
answer = bisection_method(1,2,0.0001)
print("x**2-x-1의 근 :",answer)

print("\n#P.35")
def weeklyPay(rate, hour) :
    money = 0 
    if hour>30 :
        money = rate*30 + 1.5*rate*(hour-30)
    else :
        money = rate*hour
    return money
rate = int(input("시급을 입력하시오 : "))
hour = int(input("근무 시간을 입력하시오 : "))
print(f"주급은 {weeklyPay(rate,hour)}")

print("\n#P.39")
def get_info() :
    name = input("이름 : ")
    age = int(input("나이 : "))
    return name, age
st_name, st_age = get_info()
print(f"이름은 {st_name}이고 나이는 {st_age}살입니다.")

print("\n#P.39")
def menu() :
    print("1. 섭씨 온도 -> 화씨 온도")
    print("2. 화씨 온도 -> 섭씨 온도")
    print("3. 종료")
    selection = int(input("메뉴를 선택하세요 : "))
    return selection

def ctof(c) :
    temp = c*9.0/5.0+32
    return temp

def ftoc(f) :
    temp = (f - 32.0)*5.0/9.0
    return temp

def input_f() :
    f = float(input("화씨 온도를 입력하시오 : "))
    return f

def input_c() :
    c = float(input("섭씨 온도를 입력하시오 : "))
    return c

def main() :
    while True :
        index = menu()
        if index == 1 :
            t = input_c()
            t2 = ctof(t)
            print(f"화씨 온도 = {t2}\n")
        elif index == 2 :
            t = input_f()
            t2 = ftoc(t)
            print(f"섭씨 온도 = {t2}\n")
        else :
            break

main()

print("\n#P.47")
def factorial(n) :
    if n == 1 :
        return 1
    else :
        return n*factorial(n-1)
    
n = eval(input("정수를 입력하시오 : "))
print(f"{n}! = {factorial(n)}")

print("\n#P.47")
def my_func() :
    x = 100 
    print(x)
my_func()

print("\n#P.49")
gx = 100
def myfunc():
    print(gx)

myfunc()
print(gx)

print("\n#P.50")
def myFunc() :
    x = 200
    print(x)
def main() :
    x=100
    print(x)
myFunc()
main()

print("\n#P.51")
gx = 100
g = 200
def myfunC() :
    gx = g
    print(gx)
myfunC()
print(gx)

print("\n#P.52")
gx = 100
g = 200
def myfuNC() :
    global gx
    gx = g
    print(gx)
myfuNC()
print(gx)