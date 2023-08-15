# 학번: 2021313031
# 이름 : 오수정
# 휴대폰 번호: 01096912347
# 시험 장소: 집


# 1
from operator import neg


print("------- 1 -------")
# 함수 fun(n)은 초를 매개변수 n으로
# 받아 시분초로 변환한 문자열을 반환한다.
# 주석처럼 결과가 출력되도록 '''''' 위치에
# 함수 fun(n)을 작성하시오. 

def fun(n):
    h = 0
    m = 0
    while n > 0 :
        n -= 60
        h += 1
    m = n
    return f"{h}:{m:02d}"

"""def fun(n):
    ''''''
    m = n//60
    h = m//60
    m = m%60
    s = n%60
    return f"{h}:{m:02d}:{s:02d}"""

print(fun(3600))    # 1:00:00
print(fun(45678))   # 12:41:18
print(fun(0))       # 0:00:00

# 2
print("------- 2 -------")
# fun(1, 2)와 같은 결과가 출력되도록 함수를 호출하는 방법 5가지를
# '''''' 위치에 완성하시오. 단, fun(1,)처럼 콤마로 끝나면 안된다.

def fun(m, y=2):
    print(m, y)

fun(1, 2)       # 1 2
fun(1)          # 1 2
fun(m=1,y=2)     # 1 2
fun(y=2, m=1)     # 1 2
fun(1, y=2)     # 1 2
fun(m=1)     # 1 2

# 3
print("------- 3 -------")
def fun(n) :
    if n == 0 :
        return 0
    num = 1
    while n > 1 :
        num *= n%10
        n //= 10
        if num == 0 :
            return 0
    return num
print(fun(12345))
print(fun(314))
print(fun(0))
        

# 4
print("------- 4 -------")
# fun(n)은 첫 줄에는 1, 다음줄은 12, 마지막 줄에는 12…n이
# 출력될 수 있는 문자열을 반환한다.
# 다음처럼 출력되도록 fun를 '''''' 위치에 일반성 있게 작성하시오.

def fun(n):
    string = ""
    for i in range(1,n+1) :
        for j in range(1,i+1):
            string += str(j)
        string += "\n"
    return string
        
        
print(fun(1))       # 1
print(fun(2))       # 1
                    # 12                  
print(fun(5))       # 1
                    # 12
                    # 123
                    # 1234
                    # 12345

# 5
print("------- 5 -------")
def fun(n) :
    return n*3
print(fun(10))
print(fun("10"))

# 6
print("------- 6 -------")
def fun(n) :
    negative = False
    if n < 0 :
        n *= -1
        negative = True
    n = list(str(n))
    for i in range(len(n)//3-1):
        n.insert(-3*(i+1)-i,",")
        
    if negative == False :
        return "".join(n) 
    else :
        return "-"+"".join(n) 

print(fun(-1000))
print(fun(123))
print(fun(123456))
print(fun(123456789))

# 7
print("------- 7 -------")
import random
def fun(n) :
    num = []
    for i in range(n) :
        num.append(random.randint(1,1000))
    print(f"{min(num)}, {max(num)}")
random.seed(1)
fun(1)
fun(100)
fun(7000)

# 8
print("------- 8 -------")
def myInt(s) :
    if s.isdigit() :
        return int(s)
    elif s[0] == "-" :
        return -1*int(s[1:])
    else : 
        return "숫자 아닌 문자"
def fun(s) :
    return myInt(s)

print(fun("1234567890"))
print(fun("-123"))
print(fun("1,000"))