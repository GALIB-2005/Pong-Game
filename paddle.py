from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.speed("fastest")

    def go_up(self):
        x=self.xcor()
        y=self.ycor()
        if y<240:
            self.goto(x,y+40)

    def go_down(self):
        x=self.xcor()
        y=self.ycor()
        if y>-240:
            self.goto(x,y-40)