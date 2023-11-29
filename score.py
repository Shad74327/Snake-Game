from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 14, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def score_track(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
