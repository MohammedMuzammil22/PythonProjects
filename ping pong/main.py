from turtle import Screen
from score_board import ScoreBoard
from paddle import Paddle
from ball import Ball
from player import Player
from time import sleep

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Ping Pong ----> by Muzammil")
screen.bgcolor("black")
screen.tracer(0)

right_scoreboard = ScoreBoard()
left_scoreboard = ScoreBoard()

right_paddle = Paddle(350,0)
left_paddle = Paddle(-350,0)

ball = Ball()

player = Player()
player.draw_dividor()
player.player1((-350,270))
player.player2((350,270))

screen.listen()

screen.onkeypress(fun=right_paddle.move_up,key="Up")
screen.onkeypress(fun=right_paddle.move_down,key="Down")
screen.onkeypress(fun=left_paddle.move_up,key="w")
screen.onkeypress(fun=left_paddle.move_down,key="s")


while right_scoreboard.score < 3 and left_scoreboard.score < 3:
    game_is_on = True
    while game_is_on:
        sleep(ball.ball_speed)
        right_scoreboard.display_score((30,260))#right
        left_scoreboard.display_score((-30,260))#left
        screen.update()
        ball.move_ball()

        # upper wall detection
        if(ball.ycor() > 275 or ball.ycor() < -275):
            ball.bounce_y()

        # detect ball hit with paddle
        if( ( ball.distance(right_paddle) < 50.0 and ball.xcor()>320) ) or ( ball.distance(left_paddle) < 50.0 and ball.xcor()< -320):
            ball.bounce_x()
          
        
        # r miss
        elif(ball.xcor()>380):
            game_is_on = False
            left_scoreboard.score += 1
            ball.home()
            ball.change_ball_direction()

            
        # l miss
        elif(ball.xcor()<-380):
            game_is_on = False
            right_scoreboard.score += 1
            ball.home()
            ball.change_ball_direction()


right_scoreboard.check_winner(right_scoreboard.score,left_scoreboard.score)


screen.exitonclick()