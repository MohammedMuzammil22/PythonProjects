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

scoreboard = ScoreBoard()

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


while scoreboard.r_score < 3 and scoreboard.l_score < 3:
    game_is_on = True
    sleep(0.5)
    while game_is_on:
        sleep(ball.ball_speed)
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
            scoreboard.l_point()
            ball.change_players_turn()

        # l miss
        elif(ball.xcor()<-380):
            game_is_on = False
            scoreboard.r_point()
            ball.change_players_turn()

scoreboard.check_winner()


screen.exitonclick()