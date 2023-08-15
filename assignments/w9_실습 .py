print("\n#1")
from cmath import log10
from math import expm1
from tkinter import *
'''
def minus() :
    global cnt
    cnt += 1
    label["text"] = str(cnt)
def plus() :
    global cnt
    cnt -= 1
    label["text"] = str(cnt)

window = Tk()
cnt = 0
b1 = Button(window, text ="감소", width = "6", height="1", command = minus)
b1.grid(row=0, column= 0)
label = Label(window, text="0", width = "6", height="1")
label.grid(row=0, column= 1)
b2 = Button(window, text ="증가", width = "6", height="1", command = plus)
b2.grid(row=0, column= 2)
window.mainloop()

print("\n#2")    
window = Tk()

l1 = Label(window, text="아이디", width = "6")
l1.grid(row=0, column= 0)
e1 = Entry(window, width = "12")
e1.grid(row=0, column= 1)
l2 = Label(window, text="패스워드", width = "6")
l2.grid(row=1, column= 0)
e2 = Entry(window, width = "12")
e2.grid(row=1, column= 1)

b1 = Button(window, text ="로그인", width = "9")
b1.grid(row=2, column= 0)
b2 = Button(window, text ="취소", width = "9")
b2.grid(row=2, column= 1)

window.mainloop()


print("\n#3")  
def bigger(event) :
    w.coords(i, 50, 25, 125, 100)
def smaller(event) :
    w.coords(i, 50, 25, 75, 50)
window = Tk()
w = Canvas(window, width=300, height=200)
i = w.create_rectangle(50, 25, 100, 75)
w.bind("<Button-1>", bigger)
w.bind("<Button-2>", smaller)
w.pack()

window.mainloop()


print("\n#4") 

def Down(event) :
    w.coords(i, 50, 50, 100, 100)

def Right(event) :
    w.coords(i, 75, 25, 125, 75)

window = Tk()
w = Canvas(window, width=300, height=200) 
i = w.create_rectangle(50, 25, 100, 75)
w.bind("<Button-1>", Down)
w.bind("<Button-2>", Right)
w.pack()


window.mainloop()


print("\n#5") 
import random
window = Tk()
canvas=Canvas(window, width=600,height=400)
canvas.pack()

class Box():
    def __init__(self,color,s1,e1,s2,e2):    
        self.id=canvas.create_rectangle(s1, e1, s2, e2,fill=color)
        self.dx=random.randint(1,300)
        self.dy=random.randint(1,300)
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
ballList = [Box(random.choice(colors), random.randint(100,300),random.randint(100,300),random.randint(100,300),random.randint(100,300)) for _ in range(10)]



window.mainloop()
'''

print("\n#1")
window = Tk()

def minus() :
    num = int(label['text'])
    num -= 1
    label['text'] = str(num)

def plus() :
    num = int(label['text'])
    num += 1
    label['text'] = str(num)

mB = Button(window, text = "감소", width = 7, height = 1, command = minus)
mB.pack(side = LEFT)
label = Label(window, text = '0', width = 7, height = 1)
label.pack(side = LEFT)
pB = Button(window, text = "증가", width = 7, height = 1, command = plus)
pB.pack(side = LEFT)

window.mainloop()

print("\n#2")
window = Tk()
def quit() :
    window.quit()
    window.destroy()
def login() :
    if e1.get() == 'sudeng' and e2.get() == '0627' :
        b1['width'] = 6
        b2['width'] = 11
        b1['text'] = '로그인 성공'
        b2['text'] = '로그아웃 및 종료'
l1 = Label(window, text = "아이디", width = 17)
l2 = Label(window, text = "비밀번호", width = 17)
l1.grid(row=0,column=0, columnspan=2)
l2.grid(row=1,column=0, columnspan=2)
e1 = Entry(window, width = 17)
e2 = Entry(window, width = 17)
e1.grid(row=0,column=2)
e2.grid(row=1,column=2)
b1 = Button(window, text = "로그인", command = login,width = 10)
b1.grid(row=2, column=0)
b2 = Button(window, text = "취소", command = quit,width = 7)
b2.grid(row=2, column=1)
window.mainloop()

print("\n#3")
window = Tk()
def smaller(event) :
    global sx,sy,ex,ey
    sx-=5
    sy-=5
    ex+=5
    ey+=5
    canvas.coords(w, sx-5,sy-5,ex+5,ey+5)
def bigger(event) :
    global sx,sy,ex,ey
    canvas.coords(w, sx+5,sy+5,ex-5,ey-5)
    sx+=5
    sy+=5
    ex-=5
    ey-=5

canvas = Canvas(width = 600, height=400)
sx,sy,ex,ey = 250,150,350,250
w = canvas.create_rectangle(sx,sy,ex,ey)
canvas.bind("<Button-1>", smaller)
canvas.bind("<Button-2>", bigger)

canvas.pack()
window.mainloop()

print("\n#4")
window = Tk()

    
def up(event) :
    global sx,sy,ex,ey
    sy -= 5
    ey -= 5
    canvas.coords(w, sx,sy,ex,ey)

def down(event) :
    global sx,sy,ex,ey
    sy+=5
    ey+=5
    canvas.coords(w, sx,sy,ex,ey)

def left(event) :
    global sx,sy,ex,ey
    sx -=5
    ex -=5
    canvas.coords(w, sx,sy,ex,ey)

def right(event) :
    global sx,sy,ex,ey
    sx +=5
    ex +=5
    canvas.coords(w, sx,sy,ex,ey)

    

canvas = Canvas(width = 600, height=400)
sx,sy,ex,ey = 200,100,350,250
w = canvas.create_rectangle(sx,sy,ex,ey)
canvas.bind("<Left>", left)
canvas.bind("<Right>", right)
canvas.bind("<Up>", up)
canvas.bind("<Down>", down)
canvas.focus_set()

canvas.pack()
window.mainloop()

