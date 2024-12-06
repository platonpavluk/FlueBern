import turtle

def create_circle(x, y, radius, color):
    t = turtle.Turtle()
    t.speed("fastest")

    t.hideturtle()
    t.penup()
    t.goto(x, y - radius)
    t.pendown()

    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()