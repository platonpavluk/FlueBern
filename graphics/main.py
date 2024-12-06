from graphics.render import graphics
from graphics.window import window

win = window.create_window(800, 800, "Window", "black")
graphics.create_circle(10, 60, 60, "blue")

window.run(win)