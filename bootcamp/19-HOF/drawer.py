from turtle import Turtle, Screen

draw = Turtle()
screen = Screen()


def move_forwards():
    draw.forward(10)


def move_backwards():
    draw.backward(10)


def turn_left():
    draw.setheading(draw.heading() + 10)


def turn_right():
    draw.setheading(draw.heading() - 10)


def clear():
    draw.clear()
    draw.penup()
    draw.home()
    draw.pendown()


screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'a')
screen.onkey(turn_right, 'd')
screen.onkey(clear, 'c')
screen.exitonclick()
