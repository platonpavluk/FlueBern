import turtle

def create_window(width, height, title="Window", bgcolor="white"):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title(title)
    screen.bgcolor(bgcolor)
    screen.tracer(0)
    return screen

def update_window():
    turtle.update()

def run(window):
    window.mainloop()
