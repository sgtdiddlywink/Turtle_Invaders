# -----------------------------------------------Import Modules--------------------------------------------------------#
from turtle import Turtle

# ----------------------------------------------------CONSTANTS--------------------------------------------------------#
# These can be adjusted as needed
BUNKER_STARTING_LOCATIONS = [[-40, -220], [-20, -220], [0, -220], [20, -220], [40, -220], [-40, -200], [-20, -200],
                             [0, -200], [20, -200], [40, -200], [-40, -240], [40, -240], [-200, -220], [-180, -220],
                             [-160, -220], [-140, -220], [-120, -220], [-200, -200], [-180, -200], [-160, -200],
                             [-140, -200], [-120, -200], [-200, -240], [-120, -240], [200, -220], [180, -220],
                             [160, -220], [140, -220], [120, -220], [200, -200], [180, -200], [160, -200], [140, -200],
                             [120, -200], [200, -240], [120, -240],
                             ]


# ----------------------------------------------------CLASS------------------------------------------------------------#
class Bunkers(Turtle):
    def __init__(self):
        super().__init__()
        self.all_bunkers = []  # Empty list to keep track of bunkers
        self.create_bunkers()  # Automatically create bunkers once class has been called

    # Method to create the bunkers
    def create_bunkers(self):
        for position in BUNKER_STARTING_LOCATIONS:
            new_bunker = Turtle()
            new_bunker.setposition(x=position[0], y=position[1])
            new_bunker.color("white")
            new_bunker.shape("square")
            new_bunker.penup()
            new_bunker.shapesize(stretch_wid=.9, stretch_len=.9)  # Adjust as needed
            self.all_bunkers.append(new_bunker)  # Add the new bunker object to the list

    # TODO Need to incorporate into rest of game and have collision detection set up
    # Method for pulling the bunkers off screen when collision is detected
    def destroy_bunker(self):
        self.goto(800, 800)  # Send the bunker off-screen when it is destroyed
