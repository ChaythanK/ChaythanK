import turtle
import random
from turtle import Turtle,Screen
import colorgram
# gf1=Turtle()
# gf2=Turtle()
# gf3=Turtle()
# gf4=Turtle()
# gf5=Turtle()
screen = Screen()
unicorn=Turtle()
# ye=screen.textinput("Bet","enter the turtle you bet on, blue,red,green,cyan,hotpink,darkorange")
unicorn.shape("turtle")
# gf2.shape("turtle")
# gf1.shape("turtle")
# gf4.shape('turtle')
# gf3.shape('turtle')
# gf5.shape('turtle')
# unicorn.color('green')
# gf1.color('blue')
# gf2.color('red')
# gf3.color('cyan')
# gf4.color('hotpink')
# gf5.color("darkorange")
# l=[]
# unicorn.pensize(5)
# gf1.pensize(5)
# gf2.pensize(5)
# gf3.pensize(5)
# gf4.pensize(5)
# gf5.pensize(5)
#
# screen.setup(width=1500, height=800)
# unicorn.penup()
# unicorn.goto(-700,-300)
# unicorn.pendown()
#
#
# gf1.penup()
# gf1.goto(-700,-200)
# gf1.pendown()
#
# gf2.penup()
# gf2.goto(-700,-100)
# gf2.pendown()
#
# gf3.penup()
# gf3.goto(-700,0)
# gf3.pendown()
#
# gf4.penup()
# gf4.goto(-700,100)
# gf4.pendown()
#
# gf5.penup()
# gf5.goto(-700,200)
# gf5.pendown()
#
# steps=random.randint(1,10)
#
# while ye and unicorn.position() != (700.0, -300.0):
#     steps = random.randint(1, 10)
#     unicorn.forward(steps)
# while ye and gf1.position() != (700.0, -200.0):
#     steps = random.randint(1, 10)
#     gf1.forward(steps)
# while ye and gf2.position() != (700.0, -100.0):
#     steps = random.randint(1, 10)
#     gf2.forward(steps)
# while ye and gf3.position() != (700.0, 0.0):
#     steps = random.randint(1, 10)
#     gf3.forward(steps)
# while ye and gf4.position() != (700.0, 100.0):
#     steps = random.randint(1, 10)
#     gf4.forward(steps)
# while ye and gf5.position()!=(700.0,200.0):
#     steps = random.randint(1, 10)
#     gf5.forward(steps)
#     steps = random.randint(1, 10)

def random_color():
    turtle.colormode(255)
    r=random.randint(1,255)
    g=random.randint(1,255)
    b=random.randint(1,255)
    return(r,g,b)
print(random_color())
li = [
    'blue', 'cyan', 'deepskyblue', 'dodgerblue', 'mediumblue', 'royalblue', 'steelblue',
    'green', 'limegreen', 'springgreen', 'mediumseagreen', 'seagreen', 'forestgreen',
    'red', 'orangered', 'tomato', 'coral', 'darkorange',
    'purple', 'mediumorchid', 'blueviolet', 'darkorchid', 'mediumvioletred',
    'pink', 'lightpink', 'hotpink', 'deeppink',
    'orange', 'sandybrown', 'chocolate', 'peru', 'saddlebrown'
]


def shapes(gordaah):
    n=3
    unicorn.pensize(15)
    for i in range(gordaah):
        for i in range(n):
            360/n
            unicorn.pendown()
            unicorn.forward(100)
            unicorn.right(360/n)
        rand_color = random.choice(li)
        unicorn.pencolor(rand_color)
        n+=1


def random_walk(bepop):
    unicorn.pensize(15)
    for i in range(bepop):
        unicorn.pendown()
        unicorn.forward(20)
        random_binary = random.randint(0, 1)
        if random_binary == 0:
            unicorn.right(90)
        else:
            unicorn.left(90)
        rand_color = random.choice(li)
        unicorn.pencolor(rand_color)

def random_walk_rgb(bepop):
    screen.setup(width=1500, height=800)
    boundary_x = 1500
    boundary_y = 800
    unicorn.pensize(15)
    for i in range(bepop):
        unicorn.pendown()
        unicorn.forward(20)
        random_binary = random.randint(0, 1)
        if random_binary == 0:
            x,y = unicorn.position()
            if -boundary_x < x < boundary_x and -boundary_y < y < boundary_y:
                    unicorn.forward(10)
            unicorn.right(90)
        else:
            x, y = unicorn.position()
            if -boundary_x < x < boundary_x and -boundary_y < y < boundary_y:
                unicorn.backward(10)
            unicorn.left(90)
        unicorn.pencolor(random_color())

def dot_paint():
    colors = colorgram.extract('polka dots.jpg', 49)
    n=0
    unicorn.penup()
    unicorn.goto(-70,100)
    unicorn.pendown()
    for color in colors:
        rgb = color.rgb
        l.append(rgb)
        proportion = color.proportion
        print(rgb)
        unicorn.pensize(20)
        unicorn.pencolor(rgb)
        unicorn.forward(1)
        unicorn.penup()
        unicorn.forward(40)
        unicorn.pendown()
        n+=1
        if n%7==0 and (n/7)%2==0:
            unicorn.left(90)
            unicorn.penup()
            unicorn.forward(40)
            unicorn.left(90)
            unicorn.forward(40)
            unicorn.pendown()

        elif n%7==0 and (n/7)%2!=0:
            unicorn.right(90)
            unicorn.penup()
            unicorn.forward(40)
            unicorn.right(90)
            unicorn.forward(40)
            unicorn.pendown()
def forwards():
    unicorn.forward(10)
def backwards():
    unicorn.backward(10)
def right():
    unicorn.right(10)
def left():
    unicorn.left(10)
def res():
    unicorn.reset()
def move_turtle():
    screen.listen()
    screen.onkey(forwards,'w')
    screen.onkey(backwards,'s',)
    screen.onkey(left,"a")
    screen.onkey(right,'d')
    screen.onkey(res,'c')



screen.exitonclick()