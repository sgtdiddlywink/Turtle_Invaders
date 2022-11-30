# -----------------------------------------------Import Modules--------------------------------------------------------#
import time
import turtle
from turtle import Turtle

# ----------------------------------------------------CONSTANTS--------------------------------------------------------#
FIRE_SPEED = 40


# ----------------------------------------------------CLASS------------------------------------------------------------#
# Turret Class
class TurretFire(Turtle):
    def __init__(self, turret_x):
        super().__init__()
        self.color("white")
        self.shape("classic")
        self.penup()
        self.seth(90)
        self.hideturtle()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.setposition(x=turret_x, y=-260)
        self.turret_state = "ready"
        self.fire_speed = FIRE_SPEED

    # Method to fire the turret
    def fire(self):
        self.showturtle()
        self.turret_state = "fire"

    def reload(self, turret_x):
        self.hideturtle()
        self.turret_state = "ready"
        self.sety(-300)
        self.setx(turret_x)
