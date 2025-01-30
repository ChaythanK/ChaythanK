from turtle import Screen,Turtle
from player_paddle import Paddle
from ball import Ball
from scribe import welcome_speech, score,increase_score_left,increase_score_right,check_fr_wins
import time

player2=Paddle((470,0))
player1=Paddle((-470,0))
screen = Screen()
screen.bgcolor('black')
screen.setup(1000,600)
ye=screen.textinput('level',"Enter a Number from Zero to Ten with Zero being the most difficult")
wait=int(ye)/100
points_left = 0
points_right = 0
balls=Ball()
score()
balls.goto(0,0)
welcome_speech()
def up():
    player2.forward(50)


def down():
    player2.backward(50)

def UP():
    player1.forward(50)


def DOWN():
    player1.backward(50)

screen.listen()
screen.onkey(up,'Up')
screen.onkey(down,'Down')

screen.onkey(UP,'w')
screen.onkey(DOWN,'s')

game_is_on=True
while game_is_on:
    time.sleep(wait)
    balls.move()
    if balls.ycor() > 280 or balls.ycor() < -280 :
        balls.bounce()
    if balls.distance(player2)<70 and balls.xcor()>470:
        balls.bounce_2()
    if balls.distance(player1)<70 and balls.xcor()<-470:
        balls.bounce_2()
    if balls.xcor()>500:
        balls.hideturtle()
        balls.goto(0, 0)
        balls.showturtle()
        time.sleep(0.5)
        balls.bounce_2()
        points_right+=1
        increase_score_left()

    if balls.xcor()<-500:
        balls.hideturtle()
        balls.goto(0, 0)
        balls.showturtle()
        time.sleep(0.5)
        balls.bounce_2()
        increase_score_right()

    check_fr_wins()





screen.exitonclick()