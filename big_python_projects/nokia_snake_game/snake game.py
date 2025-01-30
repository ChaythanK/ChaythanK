from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
import time
MODE = 20
snake = Snake()
score=Scoreboard()
from food import Food
food = Food()
screen = Screen()
screen.tracer(0)
screen.title('                                                                                                           Snake Game')
screen.bgcolor('black')
ye=screen.textinput("modes","type 1 for hard mode and 2 for easy mode-")
if ye == "1":
    speed = 0.09
elif ye=="2":
    speed=0.15

time.sleep(3)
def move_turtle():
    screen.listen()
    screen.onkey(snake.forwards, 'Up')
    screen.onkey(snake.backwards, 'Down', )
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, 'Right')


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    move_turtle()
    if snake.head.distance(food)<MODE:
        food.refresh()
        score.increase_score()
        snake.extend()
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 330 or snake.head.ycor() < -330:
        time.sleep(1)
        score.reset_score()
        snake.head.goto(1000,1000)
        snake.again()
    for segment in snake.segments:
        if segment==snake.head:
            pass
        elif snake.head.distance(segment)<10:
            time.sleep(1)
            score.reset_score()
            snake.again()


screen.exitonclick()

