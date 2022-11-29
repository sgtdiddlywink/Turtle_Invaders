# -----------------------------------------------Import Modules--------------------------------------------------------#
from turtle import Turtle

# ----------------------------------------------------CONSTANTS--------------------------------------------------------#
# Can adjust the moving speed of the invaders
INVADER_MOVE_DISTANCE = 20
# Add more invaders according to their onscreen location
INVADER_STARTING_LOCATIONS = [[-180, 220], [-120, 220], [-60, 220], [0, 220], [60, 220], [120, 220],
                              [180, 220]
                              ]
# Boundaries for the invaders to detect
POSITIVE_X_BOUNDARY = 380
NEGATIVE_X_BOUNDARY = -380
GROUND_BOUNDARY = -240

# ----------------------------------------------------CLASS------------------------------------------------------------#


# Invader Class
class Invaders(Turtle):
    def __init__(self):
        super().__init__()
        self.all_invaders = []  # Create empty list to add new invaders to
        self.spawn_invaders()  # Spawn the invaders once an object has been created

    def spawn_invaders(self):
        # Set attributes for each invader object
        for position in INVADER_STARTING_LOCATIONS:
            new_invader = Turtle()
            new_invader.color("red")
            new_invader.shape("turtle")
            # TODO Look into way of keeping invaders facing South at all times
            new_invader.seth(0)  # Start with objects facing East
            new_invader.penup()
            new_invader.shapesize(stretch_len=2.25, stretch_wid=2.25)  # Can adjust size of invaders here
            new_invader.goto(x=position[0], y=position[1])  # Takes input from starting position list
            self.all_invaders.append(new_invader)  # Append each new invader object ot the list

    # TODO needs work. Current bug that messes with the movement
    # Move function for the invaders
    def move_invader(self):
        invader_speed = INVADER_MOVE_DISTANCE  # Needed to add variable here to adjust
        for invader in self.all_invaders:  # Apply to each individual invader object
            invader.forward(INVADER_MOVE_DISTANCE)  # Move invader forward
            if invader.xcor() > POSITIVE_X_BOUNDARY:  # Once boundary has been hit, move down one, and then opposite way
                for invader1 in self.all_invaders:
                    invader1.right(90)
                    invader1.forward(invader_speed)
                    invader1.right(90)
            if invader.xcor() < NEGATIVE_X_BOUNDARY:
                for invader1 in self.all_invaders:
                    invader1.left(90)
                    invader1.forward(invader_speed)
                    invader1.left(90)

    # TODO needs to be worked on
    # Method to return a false statement if invaders hit lower boundary
    def invaders_reach_ground(self):
        if self.ycor() < GROUND_BOUNDARY:
            return True
        else:
            return False
