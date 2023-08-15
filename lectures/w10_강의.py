print("\n제11장 내장함수, 람다식, 제너레이터, 모듈\n")

#응 쥬피터 여기부터 다 쥬피터!!!!

print("#P.14")
def square(n):
    return n*n

mylist= [1, 2, 3, 4, 5]
result = list(map(square, mylist))
print(result)

print("\n#P.18")
def myfilter(x):  
    return x > 3  
    
result = filter(myfilter, (1, 2, 3, 4, 5, 6))  
print(list(result))

print("\n#P.21")
students = [
    ('홍길동', 3.9, 20160303),
    ('김철수', 3.0, 20160302),
    ('최자영', 4.3, 20160301),]
print(sorted(students, key=lambda student: student[2]))

print("\n#P.22")
print(sorted(students, key=lambda student: student[2]))


print("\n#P.24")
print("[<이름: 홍길동, 나이: 20>, <이름: 김철수, 나이: 35>, <이름: 최자영, 나이: 38>]")

print("\n#P.26")
print("정수의 합 : 30\n정수의 합 : 40")
print("정수의 합 : 30\n정수의 합 : 40")


print("\n#P.28")
print("[2, 4, 6, 8, 10] [2, 4, 6, 8, 10] [2, 4, 6, 8, 10]")

print("\n#P.29")
print("[2, 4, 6]")
print("[(1, 200), (3, 100), (6, 400), (7, 300)]")

print("\n#P.30")
print("10")

print("\n#P.31")
print("[-17.77777777777778, -12.222222222222223, -6.666666666666667, -1.1111111111111112, 4.444444444444445, 10.0]")