# -----------------------------------------------Import Modules--------------------------------------------------------#
from turtle import Turtle

# ----------------------------------------------------CONSTANTS--------------------------------------------------------#
FONT = ("Courier", 24, "normal")


# ----------------------------------------------------CLASS------------------------------------------------------------#
# Class to show the amount of lives the player has and keep track of them
class Lives(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.hideturtle()
        self.penup()
        self.goto(280, 260)
        self.color("white")
        self.update_lives()

    # Method to update the amount of lives the player has after being hit
    def update_lives(self):
        self.clear()
        self.write(f"Lives: {self.lives}", align="right", font=FONT)

    # Method to lose a life when collision is detected between invaders and player
    def lose_life(self):
        self.lives -= 1
        self.update_lives()
