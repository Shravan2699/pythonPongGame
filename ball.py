from turtle import Turtle,Screen
from paddles import Paddle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.my_x = 10
        self.my_y = 10
        self.move_speed = 0.1

    def ball_movement(self):
        self.speed("slowest")
        new_x = self.xcor() + self.my_x
        new_y = self.ycor() + self.my_y
        self.goto(new_x,new_y)

    def bounce_y(self):
            self.my_y *= -1

    def bounce_x(self):
            self.my_x *= -1
            self.move_speed *= 0.9

    def reset(self):
            self.goto(0,0)
            self.bounce_x()
            self.move_speed = 0.1



