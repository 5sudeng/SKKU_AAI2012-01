print("\n제3장 조건문\n")

print("#P.8")

price = int(input("상품의 가격: "))

if price > 20000 :
    shipping_cost = 0
else :
    shipping_cost = 3000

print("배송비 =",shipping_cost)

print()

print("#P.12")

radius = 100 
flag = (radius > 32)
print(flag)

print()

print("#P.14")
from math import sqrt

n = sqrt(3.0)
if abs(n*n - 3.0) < 0.00001 :
    print("sqrt(3.0)*sqrt(3.0)은 3.0과 같다.\n")
else :
    print("sqrt(3.0)*sqrt(3.0)은 3.0과 같지 않다.\n")

print()

print("#P.16")
import random

x = random.randint(1,100)
y = random.randint(1,100)

answer = int(input(f"{x}+{y}="))

flag = (answer == (x+y))

print(flag)

print()
print()

print("#P.18")

x = int(input("첫 번째 수="))
y = int(input("두 번째 수="))
max_value = (x if x>y else y)
min_value = (x if x<y else y)
print("큰 수 =",max_value,"작은 수 =",min_value)

print()
print()

print("#P.20")

number = int(input("정수를 입력하시오 : "))

if number % 2 == 0 :
    print("짝수입니다.\n")
else :
    print("홀수입니다.\n")

print()

print("#P.22")
price = int(input("정가를 입력하시오 : "))
if price >=100 :
    dis_rate = 0.85
    print("10층에서 사은품 받아가세요.")
else :
    dis_rate = 0.90
dis_price = dis_rate*price
print("할인된 상품의 가격 =",dis_price)

print()

print("#P.25")
price = int(input("가격을 입력하시오 : "))
card = input("카드 종류를 입력하시오 : ")

if price > 20000 and card == "python" :
    print("배송료가 없습니다.\n")
else :
    print("배송료는 3000원 입니다.\n")

print("#P.26")

import random
print("동전 던지기 게임을 시작합니다.")
coin = random.randrange(2)
if coin == 0 :
    print("앞면입니다.")
else :
    print("뒷면입니다.")
print("게임이 종료되었습니다.\n")

print("#P.29")
country = input("배송지(현재는 korea와 us만 가능) : ")
price = int(input("상품의 가격 : "))

if country == "korea" :
    if price >= 20000 :
        shipping_cost = 0
    else :
        shipping_cost = 3000
else :
    if price >= 100000 :
        shipping_cost = 0
    else :
        shipping_cost = 8000

print("배송비 = %d\n"%shipping_cost)

print("#P.33")
scale = float(input("리히터 규모를 입력하시오 : "))
if scale >= 8.0 :
    print("대부분의 구조물이 파괴됩니다.\n")
elif scale >= 7.0 :
    print("지표면에 균열이 발생합니다.\n")
elif scale >= 4.0 :
    print("빈약한 건물에 큰 피해가 있습니다.\n")
elif scale >= 2.0 :
    print("물건들이 흔들리거나 떨어집니다.\n")
else :
    print("지진계에 의해서만 탐지 가능합니다.\n")

print("#P.35")
print("행운의 매직볼로 오늘의 운세를 출력합니다.")
answers = random.randint(1,8)
if answers == 1 :
    print("확실히 이루어집니다.\n")
elif answers == 2:
    print("좋아 보이네요.\n")
elif answers == 3:
    print("믿으셔도 됩니다.\n")
elif answers == 4:
    print("저의 생각에는 no입니다.\n")
else :
    print("다시 질문해주세요.\n")

print("#P.37")
print("="*24)
print("""메뉴 1번 : 치즈버거
메뉴 2번 : 치킨 버거
메뉴 3번 : 불고기 버거""")
print("="*24)

selection = int(input("\n메뉴를 선택하세요 : "))
if 1<= selection <=3 :
    print("메뉴 %s\n"%selection)
else :
    print("잘못 입력하셨습니다.\n")

print("#P.38")
a = int(input("삼각형의 한 변을 입력하시오 : "))
b = int(input("삼각형의 한 변을 입력하시오 : "))
c = int(input("삼각형의 한 변을 입력하시오 : "))
if (a+b)>c and (a+c)>b and (b+c)>a :
    print("올바른 삼각형\n")
else :
    print("올바르지 않은 삼각형\n")

print("\n제4장 반복문\n")

print("#P.13")
slist = ['영어','수학','사회','과학']
slist[-1] = "컴퓨터"
print(slist)

print()

print("#P.19")
for i in range(1,6,1) :
    print(i,end = " ")
print()
for i in range(10,0,-1) :
    print(i, end=" ")

print()

print("#P.20")
sum = 0
n = 10
for i in range(1, n+1) :
    sum += i
print(f"합 = {sum}\n")
for i in range(1,6) :
    print(f"9 * {i} = {9*i}")

print()

print("#P.21")
n = int(input("정수를 입력하시오 : "))
fact = 1
for i in range(1, n+1) :
    fact *= i
print(f"{n}!은 {fact}이다.\n")

print("#P.24")
count = 100
start = 1.0
end = 2.0

for i in range(count) :
    x = start + i*((end-start)/count)
    f = x**2 - x - 1
    if abs(f-0.0) < 0.01 :
        print("방정식의 해는",x)

print()

print("#P.27")
target = 2000 #목표금액
money = 1000
year = 0
rate = 0.07

while money < target :
    money += money*rate
    year += 1

print(f"{year}년\n")

print("#P.29")
i = 1
sum = 0
while i <= 10 :
    sum += i
    i += 1

print("합계는 {}".format(sum))
