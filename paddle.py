from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(pos, 0)
        self.setheading(90)
    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)