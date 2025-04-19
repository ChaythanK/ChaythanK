# from tkinter import *
# import turtle
# import time
# fonts = [
#     "Arial", "Courier", "Courier New", "Comic Sans MS", "Fixedsys", "MS Sans Serif",
#     "MS Serif", "Symbol", "System", "Times", "Times New Roman", "Verdana", "Helvetica",
#     "Georgia", "Palatino", "Trebuchet MS", "Lucida Console", "Lucida Sans Unicode",
#     "Impact", "Tahoma", "Garamond", "Bookman", "Candara", "Century Gothic", "Consolas",
#     "Cambria", "Corbel", "Franklin Gothic Medium", "Rockwell", "Segoe UI", "Calibri"
# ]
# t = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("light blue")
# screen.title("birthday card")
# # t.pencolor("yellow")
# # print(t.xcor(),t.ycor())
# # t.pensize(60)
# # t.circle(30)
# # t.pensize(10)
# # for i in range(2):
# #     t.left(230)
# #     t.forward(30)
# #     t.fillcolor("purple")
# #     t.begin_fill()
# #     t.pencolor("purple")
# #     t.circle(50)
# #     t.end_fill()
# #
# # time.sleep(2)
# # t.goto(0.0,0.0)
# # t.pensize(60)
# #
# # t.right(20)
# # t.penup()
# # t.forward(70)
# # t.pendown()
# # t.fillcolor("purple")
# # t.begin_fill()
# # t.pencolor("purple")
# # t.circle(50)
# # t.end_fill()
# #
# # t.right(100)
# # t.penup()
# # t.forward(40)
# # t.pendown()
# # t.fillcolor("purple")
# # t.begin_fill()
# # t.pencolor("purple")
# # t.circle(50)
# # t.end_fill()
# #
# # t.right(50)
# # t.penup()
# # t.forward(60)
# # t.pendown()
# # t.fillcolor("purple")
# # t.begin_fill()
# # t.pencolor("purple")
# # t.circle(50)
# # t.end_fill()
# #
# # time.sleep(2)
# # t.goto(0.0,0.0)
# # t.pencolor("yellow")
# # t.pensize(60)
# # t.circle(30)
#
#
# t.speed(0)
# for i in range(12):
#     t.pensize(10)
#     t.pencolor("yellow")
#     t.circle(40, 30, 10)
#     t.right(100)
#     t.fillcolor("purple")
#     t.pencolor("purple")
#     t.begin_fill()
#     t.circle(10)
#     t.end_fill()
#     t.left(100)
# t.pencolor("yellow")
# t.circle(40, 30, 10)
# t.fillcolor("orange")
# t.begin_fill()
# t.circle(40)
# t.end_fill()
#
#
# ct = -1
# window = Tk()
# window.title("my first goey program")
# window.minsize(500,600)
# label = Label(text="Happy Birthday", font=("Times New Roman",50,"underline","bold"))
# window.configure(background="light blue")
# label.pack()
# def button_click():
#     global ct
#     global label
#     global fonts
#     ct+=1
#     if ct>30:
#         ct = 0
#     label.config(font=(fonts[ct],50,"underline","bold"))
#     print(ct)
# button = Button(text="click me", command=button_click)
# button.pack()
# def button_clicky():
#     t.speed(0)
#     t.clear()
#     screen.setup(1000,1000)
#     t.up()
#     t.goto(0,0)
#     t.forward(500)
#     t.backward(1000)
#
# button1 = Button(text="next page>>", command=button_clicky)
# button1.pack(side="left")
# window.mainloop()
import turtle
import random

# Setup turtle and screen
t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
screen.title("test")

# Screen properties
screen.bgcolor("black")
screen.setup(1900, 900)

# Set pen size
t.pensize(20)

# Get screen boundaries
screen_width = screen.window_width() // 2
screen_height = screen.window_height() // 2

# Generate random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    screen.colormode(255)
    return r, g, b

# Movement functions with boundary checks
def forward():
    t.setheading(90)
    if t.ycor() + 20 < screen_height:
        t.forward(20)
    t.pencolor(random_color())

def backward():
    t.setheading(270)
    if t.ycor() - 20 > -screen_height:
        t.forward(20)
    t.pencolor(random_color())

def left():
    t.setheading(180)
    if t.xcor() - 20 > -screen_width:
        t.forward(20)
    t.pencolor(random_color())

def right():
    t.setheading(0)
    if t.xcor() + 20 < screen_width:
        t.forward(20)
    t.pencolor(random_color())

# Movement loop
choices = ["forward", "backward", "left", "right"]
while True:
    choice = random.randint(0, 3)
    if choice == 0:
        forward()
    elif choice == 1:
        backward()
    elif choice == 2:
        right()
    elif choice == 3:
        left()

screen.mainloop()

