from turtle import Turtle,Screen
import turtle
from land_masses import road,track,grass,background,tree
import random
import time
screen=Screen()
chicken=Turtle()
screen.tracer(0)
li=[]
#road ^
#train
l=[]
road_choices=[
    1,
    1,
    1,
    2,
    2,
    2,
    4,
    6,
]
track_choices=[
    1,
    1,
    2,
    2,
    4,
]
units=-4
units+=1
units+=1
units+=1
hight = random.randint(10, 20)
palce = (random.randint(-1280, -100), random.randint(-200, -100))
tree((500, -200), hight)
hight = random.randint(10, 20)
tree((-500, -200), hight)
background.hideturtle()
for i in range(4):
    a=random.randint(1,5)
    if a==1 or a==2 or a==3:
        for i in range(random.choice(road_choices)):
            road(units*100)
            units+=1
    elif a==4 or a==5:
        for i in range(random.choice(track_choices)):
            track(units*100)
            units+=1
    units+=1
chicken.setheading(90)
chicken.penup()
chicken.sety(-300)
chicken.shape('turtle')
chicken.color("blue")
chicken.shapesize(2,2)
screen.update()
screen.tracer(1)
def move():
    chicken.forward(70)
    if chicken.ycor() >= 400:
        screen.tracer(0)
        screen.tracer(0)
        background.clear()
        units=-3
        chicken.sety(-370)
        for i in range(4):
            a = random.randint(1, 5)
            if a == 1 or a == 2 or a == 3:
                for i in range(random.choice(road_choices)):
                    road(units * 100)
                    units += 1
                    for i in range(9):
                        new_vehicle = Turtle("square")
                        new_vehicle.penup()
                        new_vehicle.color(random_color())
                        new_vehicle.setheading(180)
                        new_vehicle.sety((units*100)-50)
                        new_vehicle.setx(random.randint(-800,800))
                        new_vehicle.penup()
                        new_vehicle.shapesize(1.5, 3)
                        li.append(new_vehicle)
            elif a == 4 or a == 5:
                for i in range(random.choice(track_choices)):
                    track(units * 100)
                    units += 1
                    for i in range(9):
                        new_vehicle = Turtle("square")
                        new_vehicle.penup()
                        new_vehicle.color(random_color())
                        new_vehicle.setheading(180)
                        new_vehicle.sety((units*100)-50)
                        new_vehicle.setx(800)
                        new_vehicle.penup()
                        new_vehicle.shapesize(5,25)
                        l.append(new_vehicle)
                units += 1
    screen.update()
screen.tracer(1)
for i in range(600):
    for elements in li:
        elements.forward(3)
        screen.update()
while True:
    screen.tracer(0)  # Turn off tracer to prevent drawing animations
    for element in li:
        element.forward(3)
    for element in l:
        element.forward(3)
    screen.update()  # Manually update the screen to reflect changes
    time.sleep(0.01)  # Adjust the delay as needed


def random_color():
    turtle.colormode(255)
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    return(r,g,b)
screen.listen()
screen.onkey(move,"Up")
screen.tracer(1)



screen.exitonclick()
