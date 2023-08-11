from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

FOOD_COLLISION_DISTANCE = 15

game_is_on = True
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
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.snake_head.distance(food) < FOOD_COLLISION_DISTANCE:
        food.generate_food()
        snake.extend_snake()
        scoreboard.increase_score()

    # Detect collision with wall.
    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or
            snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
