from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_p1 = 0
        self.score_p2 = 0
        self.penup()
        self.color("white")
        self.goto(-70,260)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score_p2}                {self.score_p1}", font=("Arial", 20, "normal"))
        self.hideturtle()

    def r_point(self):
        self.score_p1 += 1
        self.update_scoreboard()

    def l_point(self):
        self.score_p2 += 1
        self.update_scoreboard()