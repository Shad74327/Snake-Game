from turtle import Screen
from snake import Snake
from score import Score
from food import Food

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        score.score_track()
        food.refresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_on = False

    for segments in snake.segment[1:]:
        if snake.head.distance(segments) < 15:
            score.game_over()
            game_on = False

screen.exitonclick()
