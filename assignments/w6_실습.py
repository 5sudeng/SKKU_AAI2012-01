print("\n#1")
myDict = {"옷":100,"신발":200,"가방":320}
print("총합계 :",sum(myDict.values()))

print("\n#2")
def sameWord(s1, s2) :
    same_word = set()
    for i in s1 :
        if i in s2 :
            same_word.add(i)
    return " ".join(list(same_word))

s1 = input("첫번째 문자열 : ")
s2 = input("두번째 문자열 : ")
print("모두 포함된 글자 :", sameWord(s1,s2))

print("\n#3")
def block(string, ban) :
    ban = ban.split()
    string = string.split()
    for i, w in enumerate(string) :
        for b in ban :
            if w == b :
                string[i] = "*"*len(b)
    return " ".join(string)

ban = input("금칙어 입력 : ")
s = input("문자열 입력 : ")
print(block(s,ban))

#s = s.replace(w,len(w)*"*")

print("\n#4")
def dateF(date) :
    date = "".join(date.split("/"))
    return date
date = input("MM/DD/YYYY 날짜 입력 : ")
print(f"'{date}' -> '{dateF(date)}'")

print("\n#5")
import random
import string
stri = list(string.ascii_letters)
pun = list(string.punctuation)
num = [i for i in range(10)]
lst = stri + pun + num
a = []
for i in range(8) :
    a.append(str(random.choice(lst)))
print(f"생성된 암호는 {''.join(a)}")