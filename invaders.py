# -----------------------------------------------Import Modules--------------------------------------------------------#
from turtle import Turtle

# ----------------------------------------------------CONSTANTS--------------------------------------------------------#
# Can adjust the moving speed of the invaders
INVADER_MOVE_DISTANCE = 5
# Add more invaders according to their onscreen location
INVADER_STARTING_LOCATIONS = [[-180, 220], [-120, 220], [-60, 220], [0, 220], [60, 220], [120, 220],
                              [180, 220]
                              ]
# Boundaries for the invaders to detect
POSITIVE_X_BOUNDARY = 280
NEGATIVE_X_BOUNDARY = -280
GROUND_BOUNDARY = -240

# ----------------------------------------------------CLASS------------------------------------------------------------#


# Invader Class
class Invaders(Turtle):
    def __init__(self):
        super().__init__()
        self.invader_speed = INVADER_MOVE_DISTANCE
        self.all_invaders = []  # Create empty list to add new invaders to
        self.spawn_invaders()  # Spawn the invaders once an object has been created

    def spawn_invaders(self):
        # Set attributes for each invader object
        for position in INVADER_STARTING_LOCATIONS:
            new_invader = Turtle()
            new_invader.color("red")
            new_invader.shape("turtle")
            new_invader.seth(270)  # Start with objects facing East
            new_invader.penup()
            new_invader.shapesize(stretch_len=2.25, stretch_wid=2.25)  # Can adjust size of invaders here
            new_invader.goto(x=position[0], y=position[1])  # Takes input from starting position list
            self.all_invaders.append(new_invader)  # Append each new invader object ot the list

    # TODO Bug that creates space between first and second invader when it hits the left wall
    # Move function for the invaders
    def move_invader(self):
        for invader in self.all_invaders:  # Apply to each individual invader object
            x = invader.xcor() + self.invader_speed
            invader.setx(x=x)
            # Once boundary has been hit, move down one, and then opposite way
            if invader.xcor() > POSITIVE_X_BOUNDARY or invader.xcor() < NEGATIVE_X_BOUNDARY:
                for invader1 in self.all_invaders:
                    y = invader1.ycor() - 40
                    invader1.sety(y=y)
                self.invader_speed *= -1

    # Method to return a false statement if invaders hit lower boundary
    def invaders_reset(self):
        self.invader_speed = INVADER_MOVE_DISTANCE * 1.1
        self.spawn_invaders()
