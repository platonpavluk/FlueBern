import turtle

keys_pressed = set()

def key_press(window, key, action):
    window.listen()
    window.onkey(action, key)