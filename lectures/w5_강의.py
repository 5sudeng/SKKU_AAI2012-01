print("\n제7장 파이썬 자료구조II\n")

print("#P.7")
fruits = ("apple","banana","grape")
print(fruits[1])

print("\n#P.8")
myList = [1,2,3,4]
myTuple = tuple(myList)
print(myTuple)

print("\n#P.9")
print(id(fruits))
fruits += ("pear","kiwi")
print(fruits)
print(id(fruits))

print("\n#P.11")
n1 = 10
n2 = 90
n1, n2 = (n2,n1)

print("\n#P.12")
print(list(enumerate(fruits)))
for index, value in enumerate(fruits) :
    print(index, value)

print("\n#P.17")
fruits_set = {"apple","banana","grape"}
size = len(fruits_set)

if "apple" in fruits_set :
    print("집합 안에 apple이 있습니다.")

print("\n#P.18")
for x in fruits_set :
    print(x, end = " ")

for x in sorted(fruits_set) :
    print(x, end = " ")
print()

print("\n#P.26")
list1 = [1,2,3,4,5,1,2,4]
print(len(set(list1)))

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
print(set(list1)&set(list2))

print("\n#P.28")
s1 = input("첫 번째 문자열 : ")
s2 = input("두 번째 문자열 : ")
list1 = list(set(s1)&set(s2))
print("\n공통적인 글자 : ",end ="")
for i in list1 :
    if i != " " :
        print(i, end = " ")
print()

print("\n#P.29")
txt = input("입력 텍스트 : ")
words = txt.split(" ")
unique = set(words)

print("사용된 단어의 개수 =",len(unique))
print(unique)

print("\n#P.32")
capitals = {"Korea":"Seoul", "USA":"Washington","UK":"London"}
print(capitals["Korea"])

print("\n#P.33")
capitals = {}
capitals["Korea"] = "Seoul"
capitals["USA"] = "Washington"
capitals["UK"] = "London"
capitals["France"] = "Paris"
print(capitals)


print("\n#P.34")
print(capitals.pop("UK"))

print("\n#P.35")
for key in capitals :
    print(key, ":", capitals[key])

print()

for key, value in capitals.items():
    print(key,":",value)

print("\n#P.36")
print(capitals.keys())
print(capitals.values())

for key in sorted(capitals.keys()) :
    print(key, end = " ")
print()

print("\n#P.37")
values = [1,2,3,4,5,6]
dic = {x : x**2 for x in values if x%2 == 0}
print(dic)

print("\n#P.38")
dic1 = {i:str(i) for i in [1,2,3,4,5]}
print(dic1)
fruits = ["apple","orange","banana"]
dic2 = {f:len(f) for f in fruits}
print(dic2)

print("\n#P.40")
english_dic = {}
english_dic["one"] = "하나"
english_dic["two"] = "둘"
english_dic["three"] = "셋"

word = input("단어를 입력하시오 : ")
print(english_dic[word])

print("\n#P.41")
def main() :
    address_book = {}
    while True :
        print()
        user = display_menu()
        if user == 1 :
            print("1.추가")
            name, number = get_contact()
            address_book[name] = number
        elif user == 2 :
            print("2.삭제")
            name = get_name()
            address_book.pop(name)
        elif user == 3 :
            print("3.검색")
            name = get_name()
            if name in address_book.keys() :
                print(name,"의 전화번호 :",address_book[name])
            else :
                print("검색한 이름이 없습니다.")
        elif user == 4 :
            print("4.출력")
            for key in sorted(address_book) :
                print(key,"의 전화번호 :",address_book[key])
        else :
            print("종료")
            break

def get_contact() :
    name = input("이름 : ")
    number = input("전화번호 : ")
    return name, number

def get_name() :
    name = input("이름 : ")
    return name

def display_menu() :
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
    select = int(input("메뉴 항목을 선택하시오 : "))
    return select

main()

print("\n#P.44")
score_dic = {
    "kim" : [99,83,95],
    "Lee" : [68,45,78],
    "Choi" : [25,56,69]}

for name, scores in score_dic.items() :
    print(name,"의 평균 성적 =",sum(scores)/len(scores))

print("\n#P.45")
text_data = "Create the highest, grandest vision possible for your life, because you become what you believe"
word_dic = {}
for w in text_data.split() :
    if w in word_dic :
        word_dic[w] += 1
    else :
        word_dic[w] = 1
for w, count in sorted(word_dic.items()) :
    print(w, "의 등장횟수 =",count)

print("\n#P.47")
print(ord("a"))
print(ord("가"))
print(chr(97))

print("\n#P.48")
s = "Monty Python"
print(s[0])
print(s[-1])

print("\n#P.50")
print(s[:2])
print(s[4:])
print(s[:2]+s[2:])
print(s[:4]+s[4:])
print(s[:])

print("\n#P.51")
message = "see you at noon"
low = message[:5]
high = message[5:]
print(low)
print(high)
reg ="980326"
print(reg[0:2]+"년")
print(reg[2:4]+"월")
print(reg[4:6]+"일")

print("\n#P.52")
word = "abcdef"
print(word)
word = "A"+word[1:]
print(word)

print("\n#P.53")
a = input("문자열을 입력하시오 : ")
b = input("문자열을 입력하시오 : ")
if (a<b) :
    print(a,"가 앞에 있음")
else :
    print(b,"가 앞에 있음")

print("\n#P.54")
x = 25
y = 98
prod = x*y
print(x,"와",y,"의 곱은",prod)
print(f"{x}와 {y}의 곱은 {prod}")

print("\n#P.55")
s = input("문자열을 입력하시오 : ")
s1 = s[::-1]
if(s == s1) :
    print("회문입니다.")
else :
    print("회문이 아닙니다.")

print("\n#P.56")
s = "i am A student"
print(s.capitalize())

s = "Breakfast At Tiffany"
print(s.lower())
print(s.upper())

print("\n#P.57")
s = input("파이썬 소스 파일 이름을 입력하시오 : ")
if s.endswith(".py") :
    print("올바른 파일 이름입니다.")
else :
    print("올바른 파일 이름이 아닙니다.")

print("\n#P.58")
s = "www.naver.com"
print(s.replace("com","co.kr"))
print(s.find(".kr"))
print(s.count("."))
s = "Let it be, let it be, let it be"
print(s.rfind("let"))

print("\n#P.59")
print("ABCabc".isalpha())
print("123".isdigit())
print("abc".islower())

print("\n#P.60")
s = " Hello, World!"
print(s.strip())

s = "#######this is ex####"
print(s.strip("#"))
print(s.lstrip("#"))
print(s.rstrip("#"))

print("\n#P.61")
s = "Welcome to Python"
print(s.split())
s = "Hello, World"
print(s.split(","))
s = "Hello, World"
print(s.split(", "))
print(list("Hello, World!"))

print("\n#P.62")
print(",".join(["apple","grape","banana"]))
print("-".join("010.9691.2348".split(".")))

print("\n#P.63")
phrase = input("문자열을 입력하시오 : ")
acronym = ""
for word in phrase.upper().split() :
    acronym += word[0]
print(acronym)

print("\n#P.64")
address = input("이메일 주소를 입력하시오 : ")
id, domain = address.split("@")

print(address)
print("아이디 :",id)
print("도메인 :",domain)

print("\n#P.65")
sentence = input("문자열을 입력gk시오 : ")
table = {"alphas" : 0, "digits" : 0, "spaces" : 0}

for i in sentence :
    if i.isalpha() :
        table["alphas"] += 1
    if i.isdigit() :
        table["digits"] += 1
    if i.isspace() :
        table["spaces"] += 1
print(table)

print("\n#P.66")
t = "Python is very easy and powerful!"
length = len(t.split(" "))
print(length)

print("\n#P.67")
import random
s = "0123456789"
passlen = 4
p = "".join(random.sample(s, passlen))
print(p)