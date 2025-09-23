import turtle as turtle_module
from random import choice

turtle_module.colormode(255)

colors_list = [
    (250, 246, 243),
    (248, 245, 246),
    (211, 154, 97),
    (52, 108, 132),
    (236, 245, 241),
    (177, 78, 33),
    (198, 143, 35),
    (117, 154, 170),
    (124, 79, 98),
    (122, 175, 158),
    (234, 239, 243),
    (229, 196, 128),
    (192, 86, 107),
    (55, 39, 20),
    (11, 51, 64),
    (193, 123, 142),
    (54, 121, 116),
    (41, 168, 127),
    (167, 21, 30),
    (225, 94, 79),
    (38, 31, 33),
    (5, 28, 26),
    (243, 164, 160),
    (80, 149, 171),
    (163, 26, 22),
    (235, 166, 171),
    (105, 124, 159),
    (23, 79, 90),
    (171, 207, 189),
    (158, 205, 214)]

draw = turtle_module.Turtle()
draw.speed('fastest')

draw.penup()
draw.hideturtle()

draw.setheading(225)
draw.forward(300)
draw.setheading(0)

for dot_count in range(1, 101):
    draw.dot(20, choice(colors_list))
    draw.forward(50)

    if dot_count % 10 == 0:
        draw.setheading(90)
        draw.forward(50)
        draw.setheading(180)
        draw.forward(500)
        draw.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
