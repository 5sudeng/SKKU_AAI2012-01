from math import *

print()

print("#1")
print("1+2+3을 계산하면 %d이 된다.\n"%(1+2+3))

print("#2")
print("닭의 수: 2")
print("돼지의 수: 3")
print("소의 수: 4")
print("전체 달기의 수: %d\n"%(2*2+3*4+4*4))

print("#3")
hour = int(input("시간을 입력하시오: "))
minu = int(input("분을 입력하시오: "))
print(hour,"시간",minu,"분은",hour*60*60+minu*60,"초입니다.\n")

print("#4")
x1 = int(input("x1="))
y1 = int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))
print("두점 사이의 거리=",sqrt((x1-x2)**2+(y1-y2)**2),"\n")

print("#5")
num = int(input("정수="))
tho = num//1000
hun = (num%1000)//100
ten = ((num%1000)%100)//10
one = (((num%1000)%100)%10)
print(tho+hun+ten+one,"\n")

print("#6")
num = input("숫자를 입력하시오: ")
num1 = num[:3]
num2 = num[3:]
print("%s,%s\n"%(num1,num2))