from turtle import Turtle
MOVE_DIST=20
STARTING_POSITIONS=[(0,0),(-20,0),(-40,0),]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    def again(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def forwards(self):
        if self.segments[0].heading() !=DOWN:
            self.segments[0].setheading(UP)

    def backwards(self):
        if self.segments[0].heading()!=UP:
            self.segments[0].setheading(DOWN)

    def right(self):
        if self.segments[0].heading() !=LEFT:
            self.segments[0].setheading(RIGHT)

    def left(self):
        if self.segments[0].heading() !=RIGHT:
            self.segments[0].setheading(LEFT)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            X = self.segments[i - 1].xcor()
            Y = self.segments[i - 1].ycor()
            self.segments[i].goto(X, Y)
        self.segments[0].forward(MOVE_DIST)
