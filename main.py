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
screen.setup(width=600, height=600)  # Set the screen dimensions
screen.bgcolor("black")  # Change screen background color
screen.title(titlestring="Turtle Invaders")  # Set the window title
# Turn turtle animation on/off with tracer function
screen.tracer(n=0)  # Tracer turned off when n = 0

# Create objects from the classes
player = GroundTurret()  # This is the turret object on the ground
turret = TurretFire(turret_x=player.xcor())  # Shot object. Takes player's x-coordinate to relocate
scoreboard = CurrentScore()  # Scoreboard object
lives = Lives()  # Lives Object
# Need to do apply collision with bunkers and add gunfire from invaders. Commented out for now
# bunkers = Bunkers()  # Bunker object
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

    # Statement to detect when the command to fire has been recieved and fire the turret
    if turret.turret_state == "fire":
        y = turret.ycor() + turret.fire_speed
        turret.sety(y=y)

    # Statement to check for collision between invaders and turret shot
    for invader in invaders.all_invaders:
        if invader.distance(turret) < 40:
            invaders.all_invaders.remove(invader)  # Remove the invader from the list
            print(invaders.all_invaders)
            invader.hideturtle()  # Hide that invader
            scoreboard.increase_score()  # Increase the score
            turret.reload(turret_x=player.xcor())  # Send turret shot back to turret
            if invaders.all_invaders == []:
                invaders.invaders_reset()
        # Check for collision between invaders and player
        if invader.distance(player) < 45:
            invaders.hideturtle()
            invaders.all_invaders == []
            invaders.invaders_reset()
            lives.lose_life()
            if lives.lives == 0:
                scoreboard.game_over()
                game_is_on = False

    # Returns the turret shot back to it's original position after hitting the back wall
    if turret.ycor() > 280:
        turret.reload(turret_x=player.xcor())  # Send turret shot back to turret

# Exit the screen when it is clicked
screen.exitonclick()
