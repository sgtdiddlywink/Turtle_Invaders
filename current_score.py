# -----------------------------------------------Import Modules--------------------------------------------------------#
from turtle import Turtle

# ----------------------------------------------------CONSTANTS--------------------------------------------------------#
FONT = ("Courier", 24, "normal")


# ----------------------------------------------------CLASS------------------------------------------------------------#
# Class for keeping track of the score
class CurrentScore(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.color("white")
        self.update_score()

    # TODO Need to tie into rest of game
    # Method for updating the scoreboard
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=FONT)

    # TODO Need to tie into rest of game
    # Method for increasing the score on the scoreboard
    def increase_score(self):
        self.score += 1
        self.update_score()

    # TODO Need to tie into rest of game. Will tie in with Lives Class
    # Method for saying game over
    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\n Final Score: {self.score}", align="center", font=FONT)
