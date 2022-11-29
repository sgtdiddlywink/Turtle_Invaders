# -----------------------------------------------Import Modules--------------------------------------------------------#
import random
from turtle import Turtle, Screen
import time
from current_score import CurrentScore
from lives import Lives
from ground_turret import GroundTurret
from invaders import Invaders
from bunkers import Bunkers
from turret_fire import TurretFire

# ---------------------------------------------Create window for the game----------------------------------------------#
screen = Screen()  # Set up screen object from the Screen Class
screen.setup(width=800, height=600)  # Set the screen dimensions
screen.bgcolor("black")  # Change screen background color
screen.title(titlestring="Turtle Invaders")  # Set the window title
# Turn turtle animation on/off with tracer function
screen.tracer(n=0)  # Tracer turned off when n = 0

# Create objects from the classes
player = GroundTurret()  # This is the turret object on the ground
turret = TurretFire(turret_x=player.xcor())  # Shot object. Takes player's x-coordinate to relocate
# TODO Need to have scoreboard update after collision trigger
scoreboard = CurrentScore()  # Scoreboard object
# TODO Need to have lives update after collision trigger
lives = Lives()  # Lives Object
bunkers = Bunkers()  # Bunker object
invaders = Invaders()  # Invader object

# Listen for certain keyboard inputs
screen.listen()
screen.onkey(player.go_left, "Left")  # Command to move player left
screen.onkey(player.go_right, "Right")  # Command to move player right
screen.onkey(turret.fire, "space")  # Command to shoot the turret

# While statement to run the game
game_is_on = True  # Set variable to keep game running
while game_is_on:
    time.sleep(.1)  # Wait a certain amount of time between screen refreshes
    screen.update()  # Update the screen after the sleep

    invaders.move_invader()  # Begin moving the invaders

    # TODO Set up detect collision between turret shots and invaders
    for invader in invaders.all_invaders:
        if invader.distance(turret) < 40:
            del invaders.all_invaders[invader]

    # Statement to detect when the command to fire has been recieved and fire the turret
    if turret.turret_state == "fire":
        y = turret.ycor() + turret.fire_speed
        turret.sety(y=y)

    # Returns the turret shot back to it's original position after hitting the back wall
    # TODO look at placing collision statement here for invaders
    if turret.ycor() > 280:
        turret.hideturtle()
        turret.turret_state = "ready"
        turret.sety(-300)
        turret.setx(player.xcor())

# Exit the screen when it is clicked
screen.exitonclick()
