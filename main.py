from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score_board import Scoreboard


WIDTH, HEIGHT = 800, 600
screen = Screen()
screen.bgcolor("black")
screen.setup(WIDTH, HEIGHT)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkeypress(l_paddle.down,"s")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(r_paddle.up,"Up")


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    # collosion with walls
    if ball.ycor() >= (HEIGHT-20)/2  or ball.ycor() <= -(HEIGHT-20)/2:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    if ball.xcor() > 380:
        score.increase_l_score()
        ball.reset_position()
   
    elif ball.xcor() < -380:
        score.increase_r_score()
        ball.reset_position()

screen.exitonclick()