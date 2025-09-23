'''
    _summary_

_extended_summary_
'''
import turtle as t
from random import randint

draw = t.Turtle()
t.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)


draw.speed('fastest')


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        draw.color(random_color())
        draw.circle(100)
        draw.setheading(draw.heading() + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
