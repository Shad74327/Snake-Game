from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.shape("circle")
        self.penup()

        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)

        self.goto(x, y)

