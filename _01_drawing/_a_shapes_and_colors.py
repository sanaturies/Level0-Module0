 
import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    t = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    t.shape('turtle')
    # Set your turtle's speed using .speed(2)
    t.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    t.color('green')
    t.pencolor('blue')
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    t.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
    t.left(90)
    t.right(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?
    for i in range(4):
        t.forward(100)
        t.left(90)
        
    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    #t.pencolor('white')
    t.goto(8,20)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    t.pencolor('blue')
    t.begin_fill()
    t.circle(50,steps=30)
    t.end_fill()
    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    for i in range(37):
        t.left(10)
        t.forward(30)
    t.color('pink')
    t.begin_fill()
    t.circle(190,steps=30)
    t.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()