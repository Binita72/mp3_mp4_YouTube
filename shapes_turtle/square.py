# Draw spiral patterns by python turtle

import turtle

# Environment settings
turtle.Screen().clear()
turtle.speed(0)
turtle.pensize(2)

# Function to draw spiral patterns per input parameters

colors = ["red", "green", "blue", "orange", "magenta", "cyan"]


# parameters based on the presented algorithm above
def Spiral(length, angle, step, min_length):
    # use changes of length as an index of the color
    while(length > min_length):
        # draw side(s) of the pattern
        turtle.color(colors[length % 6])
        # turn left an amount of "angle"
        turtle.forward(length)
        # then, reduce the length and get a new length in each time
        turtle.left(angle)
        length = length - step

# Call to tet the function above with necessary parameters


Spiral(length=250, angle=89, step=1, min_length=32)
input()
