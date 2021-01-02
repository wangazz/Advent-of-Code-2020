import os
import re

input_path = '../Inputs/Day-20.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

tiles = {}

new_tile = []
tile_id = int()
for line in inputs:
    if 'Tile' in line:
        find_id = re.findall('Tile (\d+):', line)
        tile_id = int(find_id[0])
    elif line != '':
        new_tile.append(line)
    else:
        tiles.update({tile_id: new_tile})
        new_tile = []

tile_count = len(tiles)

def rotate(tile):
    pass