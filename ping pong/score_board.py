from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial",30,"normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        
   
    def display_score(self,position):
        self.penup()
        self.goto(position)
        self.clear()
        self.write(f"{self.score}",align=ALIGNMENT,font=FONT)


    def check_winner(self,right_score,left_score):
        self.goto(0,0)
        self.write(f"Game Over",align=ALIGNMENT,font=FONT)
        if(right_score >left_score):
            player = 2
        else:
            player = 1
        self.goto(0,-40)
        self.write(f"player {player} wins",align=ALIGNMENT,font=FONT)
                



