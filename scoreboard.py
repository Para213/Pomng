from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.scor_l = 0
        self.scor_r = 0
        self.write(f'{self.scor_l} | {self.scor_r}', align='center', font=('Arial', 20))

    def left(self):
        self.scor_l += 1
        self.clear()
        self.write(f'{self.scor_l} | {self.scor_r}', align='center', font=('Arial', 20))

    def right(self):
        self.scor_r += 1
        self.clear()
        self.write(f'{self.scor_l} | {self.scor_r}', align='center', font=('Arial', 20))