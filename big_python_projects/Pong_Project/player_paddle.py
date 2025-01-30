from turtle import Turtle
class Paddle(Turtle,):
    def __init__(self, position):
        super(). __init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.goto(position)
        self.shapesize(1, 5)
        self.setheading(90)