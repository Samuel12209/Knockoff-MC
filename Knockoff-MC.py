from ursina import *

app = Ursina()

gravity = 0.1
jump_height = 0.2

player = Entity(
    model = 'cube' ,
    color = color.green,
    scale_y = 2
    )

def update():
    player.x += held_keys['d'] * .1
    player.x -= held_keys['a'] * .1
    player.y += held_keys['w'] * .1
    player.y -= held_keys['s'] * .1

app.run()