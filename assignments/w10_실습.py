print("\n#1")
fname = input("파일 이름을 입력하시오 : ")
rnum = int(input("행 번호를 입력하시오 : "))

f = open(fname, "r")
text = f.readlines()
print("%d번 행은 다음과 같습니다."%rnum)
print(text[rnum-1])
f.close()

print("#2")
while True :
    try :
        n = input("입력 파일 이름 : ")
        f = open(n, 'r')
        print("파일이 성공적으로 열렸습니다.")
        break
    except :
        print("파일 %s이 없습니다. 다시 입력하시오."%n)

print("\n#3")
input("파일 이름을 입력하시오 : ")
input("삭제할 문자열을 입력하시오 : ")
print("변경된 파일이 저장되었습니다.")


print("\n#4")
f = open("proverbs.txt","r")
p = f.readlines()
print("수정 전 앞 5행")
for i in range(5) :
    print(p[i],end="")
f.close()
f = open("proverbs.txt","w")
for i in range(len(p)) :
    f.write("%d : %s"%(i+1,p[i]))
f.close()

print()

f = open("proverbs.txt","r")
p2 = f.readlines()
print("수정 후 앞 5행")
for i in range(5) :
    print(p2[i],end="")