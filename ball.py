from turtle import Turtle
SPEED=15

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.x_move=SPEED
        self.y_move=SPEED
        self.movespeed=.1
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce(self):
        self.y_move *=-1
    
    def bouncep(self):
        self.x_move *=-1
        self.movespeed *=0.9
    def reset_ball(self):
        self.goto(0,0)
        self.bouncep()