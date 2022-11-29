# -----------------------------------------------Import Modules--------------------------------------------------------#
from turtle import Turtle

# ----------------------------------------------------CONSTANTS--------------------------------------------------------#
TURRET_STARTING_POSITION = (0, -280)
TURRET_MOVE_DISTANCE = 10
TURRET_FIRING_SPEED = 10


# ----------------------------------------------------CLASS------------------------------------------------------------#
# Class for creating the player
class GroundTurret(Turtle):
    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("triangle")
        self.penup()
        self.go_to_start()
        self.seth(90)  # Set the heading of the object towards the North

    # Method to move player left
    def go_left(self):
        x = self.xcor() - TURRET_MOVE_DISTANCE
        y = self.ycor()
        self.goto(x=x, y=y)

    # Method to move player right
    def go_right(self):
        x = self.xcor() + TURRET_MOVE_DISTANCE
        y = self.ycor()
        self.goto(x=x, y=y)

    # TODO Need to tie into rest of game
    # Method to put the turret back to the starting location after winning or losing
    def go_to_start(self):
        self.goto(TURRET_STARTING_POSITION)

