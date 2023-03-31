from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",14,"normal")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,-390)
        self.pensize(2)
        self.setheading(90)

    def draw_dividor(self):
        self.pendown()
        while(self.ycor() < 390):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
    
    def player1(self,position):
        self.penup()
        self.goto(position)
        self.write(f"Player 1",align=ALIGNMENT,font=FONT)
    
    def player2(self,position):
        self.penup()
        self.goto(position)
        self.write(f"Player 2",align=ALIGNMENT,font=FONT)

