from graphics.render import graphics
from graphics.window import window
from input import input

x = 50
y = 50
radius = 60
speed = 10

win = window.create_window(800, 800, "Window", "white")

circle, x, y, radius = graphics.create_circle(x, y, radius, "blue")

def move_up():
    global y, x, radius
    y += speed
    x, y, radius = graphics.update_pos(circle, x, y, radius)
    print("Key")

def move_down():
    global y, x, radius
    y -= speed
    x, y, radius = graphics.update_pos(circle, x, y, radius)

def move_left():
    global y, x, radius
    x -= speed
    x, y, radius = graphics.update_pos(circle, x, y, radius)

def move_right():
    global y, x, radius
    x += speed
    x, y, radius = graphics.update_pos(circle, x, y, radius)

input.key_press(win, "Up", move_up)
input.key_press(win, "Down", move_down)
input.key_press(win, "Left", move_left)
input.key_press(win, "Right", move_right)
graphics.add_texture_to_screen(win, "text.png", 0, 0)

window.run(win)
