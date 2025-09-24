from random import randint
from turtle import Turtle, Screen

is_race_on = False

draw = Turtle()
screen = Screen()
screen.setup(width=1700, height=400)

initial_y = 75

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']

user_bet = screen.textinput(
    title='Make your bet', prompt='Who do you think is going to win the race? Enter a color:')

turtles = []

for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.speed('fastest')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-835, y=initial_y)
    initial_y = initial_y - 25
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 815:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(
                    f"You have won! The {winning_color} turtle is the winner")
            else:
                print(
                    f"You have lost! The {winning_color} turtle is the winner")

        random_distance = randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
