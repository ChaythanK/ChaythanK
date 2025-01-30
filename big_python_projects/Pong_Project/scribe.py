from turtle import Turtle
import time
scribler=Turtle()
scriby=Turtle()
scrobe=Turtle()
scrobe.speed('fastest')
def welcome_speech():
    scribler.pencolor('white')
    scriby.pencolor('white')
    scriby.hideturtle()
    scribler.hideturtle()
    scriby.penup()
    scriby.pensize(10)
    scriby.goto(0,285)
    scriby.setheading(270)
    for i in range(0,50):
        scriby.pendown()
        scriby.forward(10)
        scriby.penup()
        scriby.forward(15)
    scribler.penup()
    scribler.goto(0,0)
    scribler.write(arg='Welcome to Pong',align='center',font=('courier', 50, 'bold'),move=False)
    time.sleep(1)
    scribler.clear()
    scribler.write(arg='Get Ready To Play', align='center', font=('courier', 50, 'bold'), move=False)
    time.sleep(1)
    scribler.clear()
    scribler.write(arg='in...', align='center', font=('courier', 50, 'bold'), move=False)
    time.sleep(1)
    scribler.clear()
    scribler.write(arg='3', align='center', font=('courier', 80, 'bold'), move=False)
    time.sleep(1)
    scribler.clear()
    scribler.write(arg='2', align='center', font=('courier', 80, 'bold'), move=False)
    time.sleep(1)
    scribler.clear()
    scribler.write(arg='1', align='center', font=('courier', 80, 'bold'), move=False)
    time.sleep(1)
    scribler.clear()
    scribler.write(arg='GO', align='center', font=('courier', 70, 'bold'), move=False)
    time.sleep(0.25)
    scribler.clear()
    
def score():
    scrobe.penup()
    global points
    global points2
    scrobe.pencolor('white')
    scrobe.pensize(9)
    points=0
    points2=0
    scrobe.goto(60,240)
    scrobe.write(arg=str(points2), align='left', font=('courier', 40, 'bold'), move=False)
    scrobe.goto(-100,240)
    scrobe.write(arg=str(points), align='left', font=('courier', 40, 'bold'), move=False)
    
def increase_score_right():
    scrobe.penup()
    global points
    global points2
    scrobe.pencolor('white')
    scrobe.pensize(8)
    scrobe.clear()
    points+=1
    scrobe.goto(60, 240)
    scrobe.write(arg=points, align='left', font=('courier', 40, 'bold'), move=False)
    scrobe.goto(-100, 240)
    scrobe.write(arg=points2, align='left', font=('courier', 40, 'bold'), move=False)


def increase_score_left():
    global points2
    global points1
    scrobe.penup()
    scrobe.pencolor('white')
    scrobe.pensize(8)
    scrobe.clear()
    points2 += 1
    scrobe.goto(-100, 240)
    scrobe.write(arg=points2, align='left', font=('courier', 40, 'bold'), move=False)
    scrobe.goto(60, 240)
    scrobe.write(arg=points, align='left', font=('courier', 40, 'bold'), move=False)

def check_fr_wins():
    if points2>=10:
        scrobe.goto(0, 0)
        scrobe.write(arg='<-you win', align='center', font=('courier', 40, 'bold'), move=False)
        time.sleep(3)
        exit()
    elif points>=10:
        scrobe.goto(0, 0)
        scrobe.write(arg='you win->', align='center', font=('courier', 40, 'bold'), move=False)
        time.sleep(3)
        exit()
        
