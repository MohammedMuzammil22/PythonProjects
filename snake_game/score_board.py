from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",16,"normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        # self.clear()
        self.write(f"SCORE : {self.score}",align=ALIGNMENT,font=FONT)
        # self.score += 1

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        # self.clear()
        self.home()
        self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)
        # self.goto(0,-30)
        # self.write(f"SCORE : {self.score}",align=ALIGNMENT,font=FONT)
