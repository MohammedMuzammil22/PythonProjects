from snake import Snake
from turtle import Screen
from time import sleep
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(height=600,width=600)
screen.title("Snake game ----> by Muzammil")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
screen.listen()

screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Food detection
    if (snake.head.distance(food) < 15):
        score_board.increase_score()
        food.update_food_location()
        snake.extend_snake()

    # wall detection
    if( snake.head.xcor() < -280 or snake.head.xcor() > 280) or (snake.head.ycor() < -280 or snake.head.ycor() > 280):
        # game_is_on = False
        # score_board.game_over()
        score_board.update_high_score()
        snake.reset()

    # tail detection
    for snake_segment in snake.snake_segments[1:]:
        if(snake.head.distance(snake_segment) < 10):
            # game_is_on = False
            # score_board.game_over()
            score_board.update_high_score()
            snake.reset()


    


screen.exitonclick()