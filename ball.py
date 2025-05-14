from turtle import Turtle
HEIGHT = 600

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.x_move = 1
        self.y_move = 1
        self.move_speed = 0.01

    def move(self):
        self.setposition(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *=0.9

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.01
        self.x_move *= -1