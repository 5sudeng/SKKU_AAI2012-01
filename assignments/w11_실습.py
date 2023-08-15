print("\n#1")
a = [i for i in range(1,101)]

n = 0

for i in a :
    if i%3 == 0 :
        n += 1

print("3의 배수의 개수 =", n)

print("\n#2")
l1 = [i for i in range(1,8)]
l2 = [i**3 for i in l1]

print("원래 리스트:")
print(l1)
print("세제곱된 값:")
print(l2)

print("\n#3")
print("0 : a\n1 : b\n2 : c")

print("\n#4")
print("원래 요소:")
print(l1)
print("제곱 후 요소:")
l3 = [i**2 for i in l1]
print(l3)

print("\n#5")
print("3\n5\n8\nTrue\nTrue\n원의 반지름 : 8")

print("\n#6")
import random
cnt = 0
al = "abcdefghijklmnopqrstuvwxyz"
for i in range(10) :
    cnt += 1
    print(random.choice(al), end = "")
    if cnt == 10 :
        break
    print(", ", end = "")
print()

