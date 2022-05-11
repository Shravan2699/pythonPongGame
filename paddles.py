from turtle import Turtle,Screen

screen = Screen()


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def paddle_pos(self,x ,y):
        self.setx(x)
        self.sety(y)


    def move_up(self):
        new_cor = 40 + self.ycor()
        self.sety(new_cor)

    def move_down(self):
        new_cor = self.ycor() - 40
        self.sety(new_cor)

