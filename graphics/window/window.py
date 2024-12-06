import turtle


def create_window(width, height, title="Window", bgcolor="white"):
    screen = turtle.Screen()
    screen.setup(width, height)
    screen.title(title)
    screen.bgcolor(bgcolor)
    return screen

def run(window):
    window.mainloop()
