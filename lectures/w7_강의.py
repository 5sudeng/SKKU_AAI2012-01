print("\n제9장 GUI 프로그래밍\n")


import imp
from pickle import DEFAULT_PROTOCOL
from tkinter import *

print("#P.6")
window = Tk()
label = Label(window, text = "Hello tkinter")
label.pack()
window.mainloop()

print("\n#P.11")
window = Tk()
button = Button(window, text = "클릭하세요!", bg = "yellow", fg = "blue", width = 20, height = 2)
button.pack()
window.mainloop()

print("\n#P.12")
window = Tk()
entry = Entry(window, fg = "black", bg = "yellow", width = 80)
entry.pack()
window.mainloop()

print("\n#P.14")
window = Tk()

label = Label(window, text = "박스 #1", bg = "red",fg = "white")
label.pack()
Label(window, text = "박스 #2", bg = "green",fg = "black").pack()
Label(window, text = "박스 #3", bg = "orange",fg = "white").pack()
window.mainloop()

window = Tk()
Button(window, text = "박스 #1", bg = "red",fg = "white").pack(side = LEFT)
Button(window, text = "박스 #2", bg = "green",fg = "black").pack(side = LEFT)
Button(window, text = "박스 #3", bg = "orange",fg = "white").pack(side = LEFT)
window.mainloop()

print("\n#P.15")
window = Tk()
b1 = Button(window, text = "박스 #1", bg = "red",fg = "white")
b2 = Button(window, text = "박스 #2", bg = "green",fg = "black")
b3 = Button(window, text = "박스 #3", bg = "orange",fg = "white")
b4 = Button(window, text = "박스 #4", bg = "pink",fg = "white")

b1.grid(row = 0, column = 0)
b2.grid(row = 0, column = 1)
b3.grid(row = 1, column = 0)
b4.grid(row = 1, column = 1)
window.mainloop()

print("\n#P.16")
window = Tk()
b1 = Button(window, text = "박스 #1", bg = "red",fg = "white")
b2 = Button(window, text = "박스 #2", bg = "green",fg = "black")
b3 = Button(window, text = "박스 #3", bg = "orange",fg = "white")
b1.place(x = 0, y = 0)
b2.place(x = 20, y = 30)
b3.place(x = 40, y = 60)
window.mainloop()

print("\n#P.17")
window = Tk()
f = Frame(window)

b1 = Button(f, text = "박스 #1", bg = "red",fg = "white")
b2 = Button(f, text = "박스 #2", bg = "green",fg = "black")
b3 = Button(f, text = "박스 #3", bg = "orange",fg = "white")
b1.pack(side = LEFT)
b2.pack(side = LEFT)
b3.pack(side = LEFT)

l = Label(window, text = "이 레이블은 버튼들 위에 배치된다.")
l.pack()
f.pack()
window.mainloop()

print("\n#P.18")
window = Tk()
window.geometry("600x100")
Button(window, text = "박스 #1", width =10, height = 1).pack()
Button(window, text = "박스 #2", width =10, height = 1).pack()
Button(window, text = "박스 #3", width =10, height = 1).pack()
window.mainloop()

print("\n#P.19")
window = Tk()
Label(window, text = "화씨").grid(row=0, column = 0)
Label(window, text = "섭씨").grid(row=1, column = 0)

e1 = Entry(window).grid(row=0, column = 1)
e2 = Entry(window).grid(row=1, column = 1)

Button(window, text = "화씨->섭씨").grid(row=2, column=1)
window.mainloop()

print("\n#P.20")
window = Tk()
Label(window, text = "너비").grid(row=0,column=0)
Label(window, text = "높이").grid(row=1,column=0)

e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

photo = PhotoImage(file = "fig3.png")
label = Label(window, image = photo)
label.grid(row = 0, column=2, columnspan=2, rowspan=2)

Button(window, text = "이미지 저장").grid(row=2, column=0, columnspan=2)

Button(window, text = "확대").grid(row=2,column=2)
Button(window, text = "축소").grid(row=2,column=3)

window.mainloop()

print("\n#P.22")
def process() :
    print("버튼이 클릭되었습니다.")

window = Tk()
button = Button(window, text = "클릭하세요!", command = process)
button.pack()

window.mainloop()

print("\n#P.23")
window = Tk()
counter = 0
def clicked() :
    global counter
    counter += 1
    label["text"] = "버튼클릭횟수 : " + str(counter)

label = Label(window, text = "아직 눌리지 않음")
label.pack()
button = Button(window, text = "증가", command = clicked).pack()
window.mainloop()

print("\n#P.25")
def process() :
    tf = float(e1.get())
    tc = (tf-32.0)*5.0/9.0
    e2.delete(0,END)
    e2.insert(0,str(tc))

window = Tk()
Label(window, text = "화씨").grid(row = 0, column = 0)
Label(window, text = "섭씨").grid(row = 1, column = 0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

Button(window, text = "화씨->섭씨", command = process).grid(row = 2, column = 1)
window.mainloop()

print("\n#P.27")
import random
answer = random.randint(1,100)

def guessing() :
    guess = int(guessField.get())

    if guess >answer :
        msg = "높음!"
    elif guess < answer :
        msg = "낮음!"
    else :
        msg = "정답!"
    
    resultLabel["text"] = msg
    guessField.delete(0,5)

def reset() :
    global answer
    answer = random.randint(1,100)
    resultLabel["text"] = "다시 한번 하세요!"

window = Tk()
window.configure(bg = "white")
window.title("숫자를 맞춰보세요!")
window.geometry("500x80")
titleLabel = Label(window, text = "숫자 게임에 오신 것을 환영합니다!", bg = "white")
titleLabel.pack()

guessField = Entry(window)
guessField.pack(side = "left")
tryButton = Button(window, text = "시도", fg = "green", bg="white", command = guessing)
tryButton.pack(side = "left")

resetButton = Button(window, text = "초기화", fg = "red", bg = "white", command = reset)
resetButton.pack(side = "left")
resultLabel = Label(window, text = "1부터 100사이의 숫자를 입력하시오.", bg = "white")
resultLabel.pack(side = "left")

window.mainloop()

print("\n#P.31")
window = Tk()
Label(window, text = "선택하세요", font = ("Helvetica","16")).pack()
frame = Frame(window)

rock_image = PhotoImage("rock.png")
paper_image = PhotoImage("paper.png")
scissors_image = PhotoImage("scissors.png")

def pass_s() :
    decide("가위")
def pass_r() :
    decide("바위")
def pass_p() :
    decide("보")

rock = Button(frame, image = rock_image, command = pass_r)
paper = Button(frame, image = paper_image, command = pass_p)
scissors = Button(frame, image = scissors_image, command = pass_s)
rock.pack(side = "left")
paper.pack(side = "left")
scissors.pack(side = "left")
frame.pack()

Label(window, text = "컴퓨터는 다음을 선택하였습니다.", font = ("Helvetica","16")).pack()
computer_image = Label(window, image = rock_image)
computer_image.pack()
output = Label(window, text = "", font = ("Helvetica","16"))
output.pack()

def decide(human) :
    computer = random.choice(["가위","바위","보"])
    if computer == "바위" :
        computer_image["image"]=rock_image
    elif computer == "보" :
        computer_image["image"]=paper_image
    else :
        computer_image["image"]=scissors_image
    
    if (computer == "바위" and human == "보") or (computer == "보" and human == "가위") or (computer == "가위" and human == "바위") :
        result = "인간 승리!"
    elif computer == human :
        result = "비겼습니다."
    else :
        result = "컴퓨터 승리!"
    output.config(text = "인간: "+ human + " 컴퓨터: "+computer+" "+result)

window.mainloop()

print("\n#P.35")
window = Tk()
window.title("My Calculator")
display = Entry(window, width=33, bg = "yellow")
display.grid(row=0,column = 0, columnspan=5)
button_list = [
    '7','8','9','/','C',
    '4','5','6','*','',
    '1','2','3','-','',
    '0','.','=','+',''
]
def click(key) :
    if key == "=" :
        result = eval(display.get())
        s = str(result)
        display.insert(END,"="+s)
    else :
        display.insert(END, key)
row_index = 1
col_index = 0

for button_text in button_list:
    Button(window, text = button_text, width = 5, command = lambda t = button_text:click(t)).grid(row = row_index, column = col_index)
    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0

window.mainloop()
print("\n#P.38")
window = Tk()
w = Canvas(window, width=300, height=200)
w.pack()
w.create_rectangle(50,25,200,100, fill = "blue")
window.mainloop()

print("\n#P.39")
window = Tk()
w = Canvas(window, width=300, height=200)
w.pack()
i = w.create_rectangle(50,25,200,100, fill = "red")

w.coords(i,0,0,100,100)
w.itemconfig(i, fill="blue")
window.mainloop()

print("\n#P.41")
window = Tk()
canvas = Canvas(window, width = 600, height = 200, bg = "#afeeee")
canvas.create_text(200, 100, fill = "darkblue", font = "Times 30 italic bold", text = "This is a text example")
canvas.pack()
window.mainloop()

print("\n#P.44")
window = Tk()
canvas = Canvas(window, width = 500, height = 300)
canvas.pack()

img = PhotoImage(file = "fig3.png")
canvas.create_image(20,20, anchor = NW, image = img)
window.mainloop()


print("\n#P.46")
WIDTH = 600
HEIGHT = 200
def displayRect() :
    canvas.create_rectangle(10,10,WIDTH-10,HEIGHT-10)
def displayOval() :
    canvas.create_oval(10,10,WIDTH-10,HEIGHT-10, fill ="yellow")
def displayArc() :
    canvas.create_arc(10,10,WIDTH-10,HEIGHT-10, start = 0, extent = 120, width = 10, fill = "blue")
def displayPolygon() :
    canvas.create_polygon(10,10,WIDTH-10,HEIGHT-10, 200, 90, 300, 160)
def displayLine() :
    canvas.create_line(10,10,WIDTH-10,HEIGHT-10, fill = "green")
def clearCanvas() :
    canvas.delete(ALL)
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg = "white")
canvas.pack()
frame = Frame(window)
frame.pack()

btRectangle = Button(frame, text = "Rectangle", command = displayRect).grid(row=1,column=2)
btOval = Button(frame, text = "Oval", command = displayOval).grid(row=1,column=3)
btArc = Button(frame, text = "Arc", command = displayArc).grid(row=1,column=5)
btPolygon = Button(frame, text = "Polygon", command = displayPolygon).grid(row=1,column=4)
btLine = Button(frame, text = "Line", command = displayLine).grid(row=1,column=1)
btClear = Button(frame, text = "Clear", command = clearCanvas).grid(row=1,column=7)

window.mainloop()

print("\n#P.49")
window = Tk() 
window.geometry("600x200")

def callback(event) :
    print(event.x, event.y, "에서 마우스 이벤트 발생")

window.bind("<Button-1>", callback)
window.mainloop()


print("\n#P.50")
window = Tk()

def key(event) :
    print(repr(event.char), "가 눌렸습니다.")
def callback(event) :
    frame.focus_set()
    print(event.x, event.y, "에서 마우스 이벤트 발생")

frame = Frame(window, width=100,height=100)
frame.bind("<Key>",key)
frame.bind("<Button-1>", callback)
frame.pack()

window.mainloop()

print("\n#P.52")
from tkinter.colorchooser import askcolor

DEFAULT_PEN_SIZE = 1.0
DEFAULT_COLOR = "black"

mode = "pen"; old_x = None; old_y = None
mycolor = DEFAULT_COLOR
erase_on = False

def use_pen() :
    global mode
    mode = "pen"

def use_brush() :
    global mode
    mode = "brush"

def choose_color() :
    global mycolor
    mycolor = askcolor(color = mycolor)[1]

def use_eraser() :
    global mode
    mode = "erase"

def paint(event) :
    global var, erase_on, mode, old_x, old_y
    fill_color = "white" if mode == "erase" else mycolor
    if old_x != None and old_y != None :
        canvas.create_line(old_x,old_y, event.x, event.y, capstyle=ROUND, width = var.get(), fill = fill_color)
    old_x = event.x
    old_y = event.y

def reset(event) :
    global old_x, old_y
    old_x, old_y = None, None

def clear_all() :
    global canvas
    canvas.delete("all")

window = Tk()
var = DoubleVar()

penButton = Button(window, text = "펜", command=use_pen)
penButton.grid(row=0, column=0, sticky=W+E)

brushButton = Button(window, text = "브러쉬", command=use_brush)
brushButton.grid(row=0, column=1, sticky=W+E)

colorButton = Button(window, text = "색상선택", command=choose_color)
colorButton.grid(row=0, column=2, sticky=W+E)

eraseButton = Button(window, text = "지우개", command=use_eraser)
eraseButton.grid(row=0, column=3, sticky=W+E)

clearButton = Button(window, text = "모두삭제", command=clear_all)
clearButton.grid(row=0, column=4, sticky=W+E)

scale = Scale(window, variable=var, orient=VERTICAL)
scale.grid(row=1,column=5,sticky=N+S)
canvas = Canvas(window, bg="white", width=600, height=400)
canvas.grid(row=1,columnspan=5)
canvas.bind("<B1-Motion>",paint)
canvas.bind("<ButtonRelease-1>",reset)

window.mainloop()

print("\n#P.56")
import time
import random

window = Tk()
canvas = Canvas(window, width=600,height=400)
canvas.pack()

class Ball() :
    def __init__(self, color, size) :
        self.id = canvas.create_oval(0,0,size, size, fill=color)
        self.dx = random.randint(1,10)
        self.dy = random.randint(1,10)

    def move(self) :
        canvas.move(self.id, self.dx, self.dy)
        x0,y0,x1,y1 = canvas.coords(self.id)
        if y1 > canvas.winfo_height() or y0 < 0 :
            self.dy *= -1
        if x1 > canvas.winfo_width() or x0 < 0 :
            self.dx *= -1

close = False

def clo(event) :
    global close 
    close = True

ball1 = Ball("blue", 60)
ball2 = Ball("green", 100)
ball3 = Ball("orange", 80)
cbtn = Button(window, text = "close")
cbtn.pack()
cbtn.bind("<Button-1>", clo)

while 1 :
    ball1.move()
    ball2.move()
    ball3.move()
    window.update()
    time.sleep(0.05)
    if close :
        window.quit()
        window.destroy()
        break

window.mainloop()

import time
print("\n#P.58")
close = False

def clo(event) :
    global close 
    close = True
window = Tk()

cbtn = Button(window, text = "close")
cbtn.pack()
cbtn.bind("<Button-1>", clo)

colors = ['red','orange','yellow','green','blue','indigo','violet']
ballList = [Ball(random.choice(colors), 60) for i in range(30)]

while True :
    for ball in ballList :
        ball.move()
    window.update()
    time.sleep(0.05)
    if close :
        window.quit()
        window.destroy()
        break

window.mainloop()