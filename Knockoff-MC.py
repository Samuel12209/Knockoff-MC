
from ursina import *
from ursina.prefabs.first_person_controller import *
import random
import math

app = Ursina()

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene,
            position=position,
            model='cube',
            origin_y=.5,
            texture='white_cube',
            color=color.hsv(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )
for i in range(1):
  angle = i
  x = 20 * math.cos(math.radians(angle))

for x in range(50):
    for y in range(1):
        for z in range(50):
            voxel = Voxel(position=(x, y, z))

for angle in range(1):
    x = 100 * math.cos(math.radians(angle)) 
    y = 0
    z = 100 * math.sin(math.radians(angle))
    voxel = Voxel(position=(x, y, z))
    voxel = Voxel(position=(x, 0, z))



for z in range(8):
    for x in range(8):
        voxel = Voxel(position=(x,0,z))


def input(key):
    if key == 'right mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            Voxel(position=hit_info.entity.position + hit_info.normal)
    if key == 'left mouse down' and mouse.hovered_entity:
        destroy(mouse.hovered_entity)

player = FirstPersonController()
app.run()