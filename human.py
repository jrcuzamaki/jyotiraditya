import turtle

def draw_body():
    # Set up the turtle
    t = turtle.Turtle()
    t.pensize(3)

    # Draw the head
    t.circle(50)

    # Draw the body
    t.right(90)
    t.forward(100)

    # Draw the legs
    t.right(30)
    t.forward(100)
    t.backward(100)
    t.left(60)
    t.forward(100)
    t.backward(100)
    t.right(30)

    # Draw the arms
    t.right(90)
    t.forward(50)
    t.left(60)
    t.forward(100)
    t.backward(100)
    t.right(120)
    t.forward(100)
    t.backward(100)
    t.left(60)
    t.backward(50)

    # Hide the turtle
    t.hideturtle()

    # Close the turtle graphics window
    turtle.done()

# Call the function to draw the body
draw_body()
