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
        with open("data.txt",mode="r") as file:
            self.high_score = int(file.read())
        self.update_score()

        


    def update_score(self):
        self.clear()
        self.write(f"SCORE : {self.score}   ||   HIGHSCORE : {self.high_score}  ",align=ALIGNMENT,font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)

    def update_high_score(self):
        if(self.score > self.high_score):
            self.high_score = self.score
            with open("data.txt",mode="w") as file:
                # file.write(str(self.high_score))
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
        
