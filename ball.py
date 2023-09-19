from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("pink")
        self.x_move = 10
        self.y_move = 10
        self.speed(1.5)

    def move(self):
        x_move = self.xcor() + self.x_move
        y_move = self.ycor() + self.y_move
        self.goto(x_move, y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1