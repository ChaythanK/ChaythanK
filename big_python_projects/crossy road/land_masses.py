from turtle import Turtle,Screen
import random
import time
WIDTH=-800
screen=Screen()
screen.tracer(0)
count=1
screen.bgcolor('lightgreen')
screen.setup(1500,800)
background=Turtle()
background.speed('fastest')
background.pencolor('lightgreen')
background.pensize(20)
def grass(a):
    WIDTH = -800
    background.pencolor('lightgreen')
    background.pensize(20)
    ct=0
    background.penup()
    background.goto(WIDTH+ct,a)
    for i in range(6):
        background.pendown()
        background.goto(WIDTH,a+ct)
        background.goto(-1*WIDTH,a+ct)
        ct+=20
        screen.update()

def tree(place,hieght):
    ct = 0
    y = 0
    count = 1
    background.penup()
    background.goto((place))
    background.pendown()
    background.pensize(20)
    background.pencolor("darkgreen")
    for i in range(14):
        background.setheading(0)
        original = (background.xcor(), background.ycor())
        background.forward(count)
        background.goto(original)
        background.backward(count)
        background.goto(original)
        background.setheading(270)
        background.forward(hieght)
        background.setheading(0)
        count += 4
        y += 8
    background.setheading(270)
    background.pensize(30)
    background.pencolor('brown')
    background.forward(20)
    screen.update()

def road(height):
    WIDTH = -800
    ct=0
    background.speed('fastest')
    background.pencolor('grey')
    background.pensize(20)
    background.penup()
    background.goto(WIDTH+ct,height)
    for i in range(6):
        background.pencolor('grey')
        background.pendown()

        background.goto(WIDTH,height+ct)
        background.goto(-1*WIDTH,height+ct)
        ct+=20
        if i==2:
            while True:
                background.setheading(180)
                background.pencolor('white')
                background.pendown()
                background.forward(20)
                background.penup()
                background.forward(40)
                if background.xcor()<-1000:
                    break
    screen.update()


#train track
def track(b):
    WIDTH = -800
    background.setheading(0)
    background.pencolor('black')
    background.pensize(20)
    ct=0
    background.penup()
    background.goto(WIDTH+ct,b)
    background.pendown()
    background.forward(1550)
    background.penup()
    background.goto(WIDTH+ct,b+80)
    background.pendown()
    background.forward(1550)
    for i in range(50):
        background.pendown()
        background.setheading(270)
        background.forward(110)
        background.backward(120)
        background.setheading(192)
        background.penup()
        background.forward(45)
        screen.update()