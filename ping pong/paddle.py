from turtle import  Turtle
from turtle import  Screen


class Paddle(Turtle):
    def __init__(self,x_cord,y_cord):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shape()
        self.color("white")
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.goto(x_cord,y_cord)

    def move_up(self):
        if(self.ycor() < 240):
            self.goto(self.xcor(),self.ycor()+20)
    def move_down(self):
        if(self.ycor() > -240):
            self.goto(self.xcor(),self.ycor()-20)
    

