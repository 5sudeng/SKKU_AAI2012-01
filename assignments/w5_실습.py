print("\n#1")
A = [i for i in range(1,11)]
B = [-1*j if j>=3 and j<=8 else j for j in range(1,11)]
print("A:",A)
print("B:",B)

print("\n#2")
lst = ["aba","xyz","abc","10001"]
cnt = 0
for word in lst :
    if word[0] == word[-1] :
        cnt += 1
print(lst)
print("문자열의 개수는",cnt)

print("\n#3")
list1 = [1,2,3,4,5,6]
list2 = [6,7,8,9,10]
print(list1)
print(list2)
for x in list1 :
    if x in list2 :
        print("True")
        break

print("\n#4")
n = int(input("n을 입력 : "))
nlist = [x for x in range(2,n+1)]
for i in range(2,n+1) :
    for x in nlist :
        if x != i and x%i == 0:
            nlist.remove(x)

print(f"2부터 {n}까지 소수는")
for j in nlist :
    print(j, end = " ")
print("\n")
