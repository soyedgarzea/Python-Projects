import time
from turtle import Turtle, Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard

screen = Screen()
screen.bgcolor('black')
screen.setup(width=1200, height=800)
screen.tracer(0)

r_paddle = Paddle((580, 0))
l_paddle = Paddle((-590, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, key='Up')
screen.onkey(r_paddle.go_down, key='Down')
screen.onkey(l_paddle.go_up, key='w')
screen.onkey(l_paddle.go_down, key='s')

game_is_on = True

while game_is_on:
    time.sleep(0.075)
    screen.update()
    ball.move()

    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 560 or ball.distance(l_paddle) < 50 and ball.xcor() < -560:
        ball.bounce_x()

    if ball.xcor() > 580:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -580:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()
