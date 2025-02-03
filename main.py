from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.listen() 
screen.tracer(0)
scoreboard=ScoreBoard()

paddle1=Paddle()
paddle1.goto(-380,0)

paddle2=Paddle()
paddle2.goto(380,0)

ball=Ball()


screen.onkey(paddle1.go_up,"w")
screen.onkey(paddle1.go_down,"s")
screen.onkey(paddle2.go_up,"Up")
screen.onkey(paddle2.go_down,"Down")

game_on=True
while game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()

    #detect collision on wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    
    # detect collision on paddle
    if ball.distance(paddle2)<50 and ball.xcor()>320 or ball.distance(paddle1)<50 and ball.xcor()<-320:
        ball.bouncep()


    # detect miss ball
    if ball.xcor()>385 :
        scoreboard.clear()
        scoreboard.increase_l()
        scoreboard.show_score()
        time.sleep(1)
        ball.reset_ball()

    if ball.xcor()<-385:
        scoreboard.clear()
        scoreboard.increase_r()
        scoreboard.show_score()
        time.sleep(1)
        ball.reset_ball()
    
    if scoreboard.lscore==5 or scoreboard.rscore==5:
        scoreboard.gameover()
        game_on=False
        
        

screen.exitonclick()