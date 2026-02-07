from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    # Detect collision with paddles
    if (ball.xcor()> 320 and ball.distance(right_paddle) < 50) or (ball.xcor() < -320 and ball.distance(left_paddle) < 50):
        ball.bounce_x()
    # Detect if ball goes out of bounds
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.left_point()
    
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()