import time
from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.extend()

    if snake.head.xcor() > 300:
        snake.moveTo(-300, snake.head.ycor())
    if snake.head.xcor() < -300:
        snake.moveTo(300, snake.head.ycor())
    if snake.head.ycor() > 300:
        snake.moveTo(snake.head.xcor(), -300)
    if snake.head.ycor() < -300:
        snake.moveTo(snake.head.xcor(), 300)

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
