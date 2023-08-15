print("\n제6장 파이썬 자료구조I(리스트)\n")

print("#P.10")
temps = [28,31,33,35,27,26,25]
for i in range(len(temps)) :
    print(temps[i], end =",")
print()

for element in temps :
    print(element, end=",")
print()

print("\n#P.11")
questions = ['name','quest','color']
answers = ['Kim','파이썬','blue']

for q,a in zip(questions,answers) :
    print(f"What is ypur {q}? It is {a}.")

print("\n#P.12")
heroes = []
heroes.append("아이언맨")
heroes.append("토르")
print(heroes)

print("\n#P.14")
n = heroes.index("토르")
print(f"토르의 index는? {n}")

print("\n#P.19")
values = []
for i in range(1,11) :
    values.append(i)

print(min(values))
print(max(values))

print("\n#P.20")
a = [3,2,1,5,4]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

print("\n#P.21")
numbers = [10,3,7,1,9,4,2,8,5,6]
ascending_numbers = sorted(numbers)
print(ascending_numbers)

print("\n#P.24")
numbers = [10,20,30,40,50]

print("합 =",sum(numbers))
print("최댓값 =",max(numbers))
print("최솟값 =",min(numbers))

print("\n#P.25")
import random

numberList = [1,2,3,4,5,6,7,8,9,10]
print("랜덤하게 선택한 항목 =",random.choice(numberList))

movie_list = ["Citizen Kane","Singin' in the Rain","Modern Times","Casablanca","City Lights"]
item = random.choice(movie_list)
print("랜덤하게 선택한 항목 =",item)

print("\n#P.26")
STUDENT = 5
lst = []
cnt = 0

for i in range(STUDENT) :
    value = int(input("성적을 입력하시오 : "))
    lst.append(value)

print("성적 평균 =",sum(lst)/len(lst))
print("최대 점수 =",max(lst))
print("최저 점수 =",min(lst))

for score in lst :
    if score >= 80 :
        cnt += 1

print("80점 이상 =",cnt)

print("\n#P.28")
list1 = [1,2,3,4,15,99]
list1.sort()
print("두 번째로 큰 수 =",list1[-2])
list1.remove(max(list1))
print("두 번째로 큰 수 =",max(list1))

print("\n#P.30")
scores = [10.0,9.0,8.3,7.1,3.0,9.0]
print("제거 전",scores)
scores.remove(max(scores))
scores.remove(min(scores))
print("제거 후",scores)

print("\n#P.31")
stack = []
for i in range(3) :
    f = input("과일을 입력하시오 : ")
    stack.append(f)
for i in range(3) :
    print(stack.pop())

print("\n#P.33")
menu = 0
friends = []
while menu != 9 :
    print("-"*15)
    print("1.친구 리스트 출력")
    print("2.친구 추가")
    print("3.친구 삭제")
    print("4.이름 변경")
    print("9.종료")
    menu = int(input("메뉴를 선택하시오 : "))
    if menu == 1 :
        print(friends)
    elif menu == 2 :
        name = input("이름을 입력하시오 : ")
        friends.append(name)
    elif menu == 3 :
        del_name = input("삭제하고 싶은 이름을 입력하시오 : ")
        if del_name in friends :
            friends.remove(del_name)
        else :
            print("이름이 발견되지 않았음")
    elif menu == 4 :
        old_name = input("변경하고 싶은 이름을 입력하시오 : ")
        if del_name in friends :
            index = friends.index(old_name)
            new_name = input("새로운 이름을 입력하시오 : ")
            friends[index] = new_name
        else :
            print("이름이 발견되지 않았음")
    elif menu == 9 :
        break
    else :
        continue

print("\n#P.37")
temps = [28,31,33,35,27,26,25]
values = temps

print(temps)
values[3] = 39
print(temps)

print("\n#P.38")
temps = [28,31,33,35,27,26,25]
values = list(temps)

print("\n#P.40")
numbers = []
num = 10
for i in range(9) :
    numbers.append(num)
    num += 10
print(numbers[:3])
print(numbers[3:])
print(numbers[:])

print("\n#P.42")
print(numbers[::-1])

print("\n#P.43")
lst = [1,2,3,4,5,6,7,8]
lst2 = list(lst)
lst3 = list(lst)
lst[0:3] = ['white','blue','red']
print(lst)

lst2[::2] = [99,99,99,99]
print(lst2)

lst3[:] = []
print(lst3)

print("\n#P.44")
numbers = list(range(0,10))
print(numbers)
del numbers[-1]
print(numbers)

print("\n#P.46")
numbers = list(range(1,11))
reserved = numbers[::-2]
print(reserved)

numbers[1:] = []
print(numbers)

print("\n#P.48")
def func2(lst) :
    lst [0] = 99
values = [0.1,1,2,3,5,8]
func2(values)
print(values)

print("\n#P.49")
salaries = [200,250,300,280,500]

def modify(values, factor) :
    for i in range(len(values)) :
        values[i] = values[i]*factor
print("인상전",salaries)
modify(salaries,1.3)
print("인상후",salaries)

print("\n#P.52")
prices = [135,-545,922,356,-992,217]
mprices = [i if i>0 else 0 for i in prices]
print(mprices)

words = ["All","good","things","must","come","to","an","end."]
letters = [w[0] for w in words]
print(letters)

numbers = [x+y for x in ['a','b','c'] for y in ['x','y','z']]
print(numbers)

print("\n#P.53")
numbers = [x for x in range(100) if x%2 == 0 and x%3 == 0]
print(numbers)

print("\n#P.54")
list1 = [x for x in range(10,51,10)]
list2 = [sum(list1[0:x+1]) for x in range(0,len(list1))]
print("원래 리스트 :",list1)
print("새로운 리스트 :",list2)

print("\n#P.55")
new_list = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]

print("\n#P.56")
s = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
print(s)

print("\n#P.57")
print(s[1])
print(s[1][2])

print("\n#P.58")
rows = 3
cols = 5

s1 = []
for row in range(rows) :
    s1 += [[0]*cols]

print(s1)

s2 = []
for row in range(rows) :
    s += [0]*cols

print(s2)

print("\n#P.59")
s3 = [([0]*cols) for row in range(rows)]
print(s3)

print("\n#P.60")
s = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]

rows = len(s)
cols = len(s[0])

for r in range(rows) :
    for c in range(cols) :
        print(s[r][c], end = " ")
    print()

print("\n#P.61")
def summ(numbers) :
    total = 0
    for i in range(len(numbers)) :
        for j in range(len(numbers[0])) :
            total += numbers[i][j]
    return total
print(summ(s))

print("\n#P.62")
table = []
def printList(mylist) :
    for row in range(len(mylist)) :
        for col in range(len(mylist[0])):
            print(mylist[row][col], end = " ")
        print()

def init(mylist) :
    for row in range(len(mylist)) :
        for col in range(len(mylist[0])):
            if (row+col)%2 == 0 :
                table[row][col] = 1


table = [[0 for x in range(10)] for j in range(10)]
init(table)
printList(table)

print("\n#P.63")
matrix = [[i for i in range(5)] for _ in range(6)]
print(matrix)

matrix = [[0,0,0], [1,1,1], [2,2,2]]
result = [num for row in matrix for num in row]
print(result)

print("\n#P.64")
transposed = []
matrix = [[1,2,3],[4,5,6], [7,8,9]]

print("원래 행렬 =", matrix)
for i in range(len(matrix[0])) :
    transposed_row = []
    for row in matrix :
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print("전치 행렬 =", transposed)

print("\n#P.65")
board = [[" " for x in range(3)] for y in range(3)]
while True :
    for r in range(3) :
        print(" "+board[r][0]+"| "+board[r][1]+"| "+board[r][2])
        if (r!=2) :
            print("--|--|--")
    x = int(input("다음 수의 x좌표를 입력하시오 : "))
    y = int(input("다음 수의 y좌표를 입력하시오 : "))
    if board[x][y] != " " :
        print("잘못된 위치입니다.")
        continue
    else :
        board[x][y] = "X"
    done = False
    for i in range(3) :
        for j in range(3) :
            if board[i][j] == " " and not done :
                board[i][j] = "O" 
                done = True 
                break
            