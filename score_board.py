from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.l_score} : {self.r_score}", align = "center", font = ("Times New Roman", 20, "normal"))

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.color("red")
        self.goto(0,0)
        self.write(f"GAME OVER !!!", align = "center", font = ("Times New Roman", 12, "normal"))