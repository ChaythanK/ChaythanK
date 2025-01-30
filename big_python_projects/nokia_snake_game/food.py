from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('blue')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        xx = random.randint(-280, 280)
        yy = random.randint(-280, 280)
        self.penup()
        self.speed('fastest')
        self.goto(xx, yy)
