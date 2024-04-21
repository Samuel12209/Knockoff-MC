from ursina import *
from ursina.prefabs.first_person_controller import *
import random
import math

app = Ursina()
current_delay = 0.9

class Voxel(Button):
    def __init__(self, position=(0,0,0)):
        super().__init__(parent=scene, 
            position=position,
            model='cube',
            origin_y=.5,
            texture='grass.png',
            color=color.hsv(0, 0, random.uniform(.9, 1.0)),
            highlight_color=color.lime,
        )

voxels = []
for x in range(50):
    for y in range(1):
        for z in range(50):
            voxel = Voxel(position=(x, y, z))
            voxels.append(voxel)

for z in range(8):
    for x in range(8):
        voxel = Voxel(position=(x,0,z))
        voxels.append(voxel)

def hills(start_x, start_z, height, radius):
    print("Hills")


tree_num = random.randrange(1, 2)
for i in range(50):
    if tree_num == 1:
        class Wood(Button):
            def __init__(self, position=(0,0,0)):
                super().__init__(parent=scene, 
                position=position,
                model='cube',
                origin_y=.5,
                texture='wood.png',
                color=color.hsv(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )

        tree_x = random.randint(0, 49)
        tree_z = random.randint(0, 49)
        voxel = Wood(position=(tree_x, 1, tree_z))
        voxel = Wood(position=(tree_x, 2, tree_z))
        voxel = Wood(position=(tree_x, 3, tree_z))
        voxel = Wood(position=(tree_x, 4, tree_z))
        voxel = Wood(position=(tree_x, 5, tree_z))
        #leaves
        class Leaf(Button):
            def __init__(self, position=(0,0,0)):
                super().__init__(parent=scene, 
                position=position,
                model='cube',
                origin_y=.5,
                texture='leaf.png',
                color=color.hsv(0, 0, random.uniform(.9, 1.0)),
                highlight_color=color.lime,
            )

        voxel = Leaf(position=(tree_x, 6, tree_z))
        voxel = Leaf(position=(tree_x + 1, 5, tree_z))
        voxel = Leaf(position=(tree_x - 1, 5, tree_z))
        voxel = Leaf(position=(tree_x, 5, tree_z + 1))
        voxel = Leaf(position=(tree_x, 5, tree_z - 1))

def input(key):
    if key == 'right mouse down':
        hit_info = raycast(camera.world_position, camera.forward, distance=5)
        if hit_info.hit:
            voxel = Voxel(position=hit_info.entity.position + hit_info.normal)
            voxels.append(voxel)
            
    if key == 'left mouse down' and mouse.hovered_entity and distance(player.position, mouse.hovered_entity.position) < 5:
        destroy(mouse.hovered_entity)

player = FirstPersonController()
player_xr = random.randint(0, 49)
player_zr = random.randint(0, 49)
player.position =  (player_xr, 100, player_zr)
app.run()