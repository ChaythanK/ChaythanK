from turtle import Turtle, Screen
import pandas
import time
scribe = Turtle()
screen = Screen()
screen.setup(730,500)
screen.bgpic('blank_states_img.gif')
scribe.hideturtle()
scribe.penup()
d = pandas.read_csv("50_states.csv")
xy = d['x'].to_list()
yx = d['y'].to_list()
states = d['state'].to_list()
ct=0
for i in range(50):
    ye = screen.textinput(f'{ct}/50', "Name a state:")
    for b in states:
        if (str(ye)).strip().lower() == str(b).lower():
            coordinates = (xy[states.index(b)],yx[states.index(b)])
            print(coordinates)
            scribe.goto(coordinates)
            scribe.write(arg=str(b), move=False, align="center", font=("Arial", 10, "bold"))
            states[states.index(b)] = 'AJKFNJKFNJ19830'
            ct+=1
        if ct>50:
            scribe.goto(0,0)
            scribe.write(arg='You Did It!!', move=False, align="center", font=("Arial", 50, "bold"))




screen.exitonclick()