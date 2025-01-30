from turtle import Turtle
FONT = ('courier', 20, 'bold')
SAD_FONT = ('courier', 40, 'bold')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor('white')
        self.clear()
        self.ht()
        self.penup()
        self.goto(-50, 280)
        self.pendown()
        self.score=0
        with open('high_scores.txt', 'r') as file:
            self.high_score = int(file.read())
        a = 'score-'+str(self.score)
        self.write(a, False, 'left', FONT)

    def reset_score(self):
        self.clear()
        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        b="high score-"+str(self.high_score)
        a = 'score-' + str(self.score)
        self.write(a, False, 'left', FONT)
        self.penup()
        self.setheading(270)
        self.forward(30)
        self.write(b, False, 'left', FONT)
        self.backward(30)
        self.setheading(0)
        with open('high_scores.txt', 'w') as file:
            file.write(str(self.high_score))
        with open('high_scores.txt', 'r') as file:
            reading = file.read()
            print(reading)




    # def game_over(self):
    #     self.goto(-100,0)
    #     self.write('GAME OVER', False, 'left', FONT)

    def increase_score(self):
        self.clear()
        self.score+=1
        b="high score-"+str(self.high_score)
        a = 'score-' + str(self.score)
        self.write(a, False, 'left', FONT)
        self.penup()
        self.setheading(270)
        self.forward(30)
        self.write(b, False, 'left', FONT)
        self.backward(30)
        self.setheading(0)