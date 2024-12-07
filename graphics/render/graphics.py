import turtle


def create_rectangle(x, y, width, height, color):
    t = turtle.Turtle()
    t.speed("fastest")
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.pendown()

    t.fillcolor(color)
    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)

    t.end_fill()


def create_circle(x, y, radius, color):
    t = turtle.Turtle()
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.begin_fill()
    t.color(color)
    t.circle(radius)
    t.end_fill()

    return t, x, y, radius


def update_pos(circle, x, y, radius):
    circle.clear()
    circle.penup()
    circle.goto(x, y - radius)
    circle.pendown()
    circle.begin_fill()
    circle.color(circle.fillcolor())
    circle.circle(radius)
    circle.end_fill()

    return x, y, radius