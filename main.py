from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

#screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pomng")
screen.tracer(0) #stops animations

l_paddle = Paddle(-350) #player 1
r_paddle = Paddle(350)  #player 2
ball = Ball() #spawn ball
scoreboard = Scoreboard() #spawn scoreboard

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    sleep(0.05)
    game_is_on = True

    #Detect collision with borders
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    # Detect collision with right paddle
    if ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect collision with out of bounds

    if ball.xcor() < -360:
        ball.home()
        scoreboard.left()
        sleep(1)

    elif ball.xcor() > 360:
        ball.home()
        scoreboard.right()
        sleep(1)

