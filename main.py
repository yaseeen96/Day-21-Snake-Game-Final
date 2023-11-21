from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

score_board = ScoreBoard()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(key="w", fun=snake.up)
screen.onkey(key="s", fun=snake.down)
screen.onkey(key="d", fun=snake.right)
screen.onkey(key="a", fun=snake.left)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect colission with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()    
        score_board.increase_score()

    # detect collission with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.game_over()
        game_is_on = False
    
    # detect collision with tail
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score_board.game_over()


screen.exitonclick()