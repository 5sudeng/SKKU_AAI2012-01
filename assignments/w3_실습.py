from math import *

print()

print("#1")
rad = float(input("원의 반지름: "))
if rad < 0 :
    print("잘못된 값입니다\n")
else :
    print("원의 면적: %.1f\n"%(rad*rad*3.14))

print("#2")
a, b, c = map(int, input("3개의 정수를 입력하시오: ").split(','))
if a < b :
    if a < c :
        min = a
    else :
        min = c
else :
    if b < c :
        min = b
    else :
        min = c
print("제일 작은 정수는 %d 입니다.\n"%min)
    
print("#3")
a = int(input("a를 입력하시오: "))
b = int(input("b를 입력하시오: "))
c = int(input("c를 입력하시오: "))

D = b*b - 4*a*c

if  D > 0 :
    ans1 = (-1*b - sqrt(D))/(2*a)
    ans2 = (-1*b + sqrt(D))/(2*a)
    print("두 실근은 %f, %f입니다.\n"%(ans1,ans2))
elif D == 0 :
    ans1 = (-1*b)/(2*a)
    print("중근은 %f입니다.\n"%ans1)
else :
    print("실근이 없습니다.\n")

print("#4")
num = int(input("정수를 입력하시오: "))

if num%3 == 0 and num%5 == 0 :
    print("Python Express\n")
elif num%3 == 0 :
    print("Python\n")
elif num%5 == 0 :
    print("Express\n")
else :
    print()

print("#5")
sum = 0
for num in range(1,101) :
    if num%3 == 0 :
        sum += num

print("1~100인 모든 3의 배수합: %d\n"%sum)

print("#6")
n = int(input("정수를 입력하시오: "))
for i in range(1,n+1) :
    for j in range(1,i+1) :
        print(j,end="")
    print()

print()