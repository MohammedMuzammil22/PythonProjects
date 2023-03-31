from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-270,260)
        self.level = 1

    def display_level(self):
        self.write(f"Level : {self.level}",font=FONT)
    
    def update_level(self):
        self.level += 1
        self.clear()
        self.display_level()
    
    def game_over(self):
        self.home()
        self.write(f"GAME OVER",font=("Courier", 30, "bold"),align="center")

    