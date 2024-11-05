import turtle

turtle.Screen().bgcolor("light blue")
screen = turtle.Screen()
t = turtle.Turtle()

side_length = 500

for _ in range(4):
    t.forward(side_length)
    t.left(450)


turtle.done()