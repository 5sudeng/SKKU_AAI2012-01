print()
'''
print("#1")
n = int(input("n의 값을 입력 : "))
sum = 0
for i in range(1, n+1) :
    sum += i*i
print(f"계산값은 {sum}입니다.\n")

print("#2")
n = int(input("몇 번째 항까지 구할까요? : "))
bef = 0
cur = 1
for i in range(n+1) :
    print(bef, end='')
    temp = bef
    bef = cur
    cur += temp
    if i == n-1 :
        print("\n")
        break
    print(", ",end="")


print("#3")
def get_peri(radius = 5.0) :
    return radius*radius*3.141592
print("get_peri() =",get_peri())
print("get_peri(4.0) =",get_peri(4.0))

print("\n#4")
def calc(x,y) :
    a = x+y
    b = x-y
    c = x*y
    d = x/y
    return a,b,c,d

num1 = int(input("첫 번쩨 정수를 입력하시오 : "))
num2 = int(input("두 번쩨 정수를 입력하시오 : "))
a,b,c,d = calc(num1, num2)
print(f"{a}, {b}, {c}, {d}이 반환되었습니다.\n")

print("#5")
def itos(num) :
    hun = num//100
    ten = (num%100)//10
    one = (num%100)%10
    dic = {1:'일',2:'이',3:'삼',4:'사',5:'오',6:'육',7:'칠',8:'팔',9:'구'}
    print(f"{dic.get(hun)}백", end =" ")
    if ten != 0 :
        print(f"{dic.get(ten)}십", end =" ")
    if one != 0 :
        print(f"{dic.get(one)}", end =" ")
    print()
num = int(input("세 자리 정수를 입력 : "))
itos(num)
'''
print("\n#6")
def dec2bin(dec) :
    num = dec
    cnt = 1
    bin = 0
    while  num >= 1:
        bin += (num % 2)*cnt
        num = num // 2
        cnt *= 10
        print(bin)
    print(bin)
        
decimal = int(input("10 진수 : "))
dec2bin(decimal)