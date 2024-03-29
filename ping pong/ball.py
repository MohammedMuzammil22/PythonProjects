from turtle import Turtle,Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
            self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.99


    def change_ball_direction(self):
        self.x_move *= -1
        self.ball_speed = 0.1

    def change_players_turn(self):
        self.home()
        self.change_ball_direction()


