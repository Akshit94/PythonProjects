import turtle

def draw_art():
    # this line creates a new windows for our turtle to work on.
    window = turtle.Screen()
    # sets the window's background color to red.
    window.bgcolor("red")
    # here "turtle" is the atual thing that moves around and draws stuff
    # on the computer for us.
    # turtle.Turtle() is used to grab the turtle. "Turtle" is a class.
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(3)
    # forward(distance) moves the turtle forward by the given distance.
    # right(degrees) turns the turtle to right by the given degrees.
    for i in range(1,37):
        count = 4
        while(count):
            brad.forward(50)
            if(count == 4 or count == 2):
                brad.right(35)
            elif(count == 3):
                brad.right(145)
            count = count - 1
        brad.right(155)
    brad.right(90)
    brad.forward(200)

    # this call defines that windows will be closed if we click on it.
    window.exitonclick()

draw_art()
