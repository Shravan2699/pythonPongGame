from turtle import Turtle,Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ball = Ball()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
scoreboard = Scoreboard()

screen = Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")

# tim = Turtle()
# tim.speed("fastest")
# tim.color("white")
# tim.penup()
# tim.goto(0,300)
# tim.right(90)
# tim.pendown()
# for i in range(20):
#     tim.forward(20)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    ball.ball_movement()
    if ball.xcor() > 370:
        ball.reset()
        scoreboard.l_point()
    if ball.xcor() < -370:
        ball.reset()
        scoreboard.r_point()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # print("contact made ")
        ball.bounce_x()
        ball.ball_movement()
    screen.update()

screen.exitonclick()