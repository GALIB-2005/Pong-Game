from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore=0
        self.rscore=0
        self.hideturtle()
        self.penup()
        self.color("Yellow")
        self.show_score()
    def increase_l(self):
        self.lscore+=1
    
    def increase_r(self):
        self.rscore+=1

    def show_score(self):
        self.goto(-100,200)
        self.write(f"{self.lscore}",align="center",font=("Arial",40,"normal"))
        self.goto(100,200)
        self.write(f"{self.rscore}",align="center",font=("Arial",40,"normal"))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",40,"normal"))