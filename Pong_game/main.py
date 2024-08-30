from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
speed = 0.1
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball((0, 0))
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320\
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed *= 0.9


    #If ball miss the right paddle
    if ball.xcor() > 365:
        ball.reset_positon()
        score.l_point()

    #if ball miss the left paddle
    if ball.xcor() < -365:
        ball.reset_positon()
        score.r_point()






screen.exitonclick()
