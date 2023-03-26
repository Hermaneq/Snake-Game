from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
new_snake = Snake()
food = Food()
new_scoreboard = Scoreboard()
screen.listen()
screen.onkey(new_snake.up, "Up")
screen.onkey(new_snake.down, "Down")
screen.onkey(new_snake.left, "Left")
screen.onkey(new_snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move()
    if new_snake.head.distance(food) < 15:
        food.refresh()
        new_snake.consumed()
        new_scoreboard.add_score()
    if new_snake.head.xcor() > 280 or new_snake.head.xcor() < -280:
        new_scoreboard.reset()
        new_snake.reset()

    elif new_snake.head.ycor() > 280 or new_snake.head.ycor() < -280:
        new_scoreboard.reset()
        new_snake.reset()

    for segment in new_snake.segments[1:]:
        if new_snake.head.distance(segment) < 10:
            new_scoreboard.reset()
            new_snake.reset()










screen.exitonclick()
