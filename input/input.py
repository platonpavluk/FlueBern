import turtle

keys_pressed = set()

def key_press(window, key, action):
    if action == "press":
        keys_pressed.add(key)  # Додаємо клавішу, коли вона натиснута
    elif action == "release":
        keys_pressed.remove(key)  # Видаляємо клавішу, коли вона відпущена
