import os
input_path = '../Inputs/Day-17.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

cycles = 6

def bounds(values):
    return (min(values) - 1, max(values) + 2)

def inactive_coordinates(active_coordinates):
    inactive_coordinates = []
    for a in active_coordinates:
        for n in neighbours(*a):
            if n not in active_coordinates:
                inactive_coordinates.append(n)
    return list(set(inactive_coordinates))

def neighbours(i, j, k, l = None):
    if l != None:
        cube = [(x, y, z, w) for x in range(i - 1, i + 2) for y in range(j - 1, j + 2) for z in range(k - 1, k + 2) for w in range(l - 1, l + 2)]
        cube.remove((i, j, k, l))
        assert len(cube) == 80
    else:
        cube = [(x, y, z) for x in range(i - 1, i + 2) for y in range(j - 1, j + 2) for z in range(k - 1, k + 2)]
        cube.remove((i, j, k))
        assert len(cube) == 26
    return cube

# Part 1: 3D
active = []
for x, line in enumerate(inputs):
    for y, char in enumerate(line):
        if char == '#':
            active.append((x, y, 0))

next_active = active.copy()
for cycle in range(cycles):
    for a in active:
        active_neighbours = 0
        for n in neighbours(*a):
            if n in active:
                active_neighbours += 1

        if not (active_neighbours == 2 or active_neighbours == 3):
            next_active.remove(a)

    inactive = inactive_coordinates(active)
    for i in inactive:
        active_neighbours = 0
        for n in neighbours(*i):
            if n in active:
                active_neighbours += 1
        if active_neighbours == 3:
            next_active.append(i)

    active = next_active.copy()

print(len(active))

# Part 2: 4D
active = []
for x, line in enumerate(inputs):
    for y, char in enumerate(line):
        if char == '#':
            active.append((x, y, 0, 0))

next_active = active.copy()
for cycle in range(cycles):
    for a in active:
        active_neighbours = 0
        for n in neighbours(*a):
            if n in active:
                active_neighbours += 1

        if not (active_neighbours == 2 or active_neighbours == 3):
            next_active.remove(a)

    inactive = inactive_coordinates(active)
    for i in inactive:
        active_neighbours = 0
        for n in neighbours(*i):
            if n in active:
                active_neighbours += 1
        if active_neighbours == 3:
            next_active.append(i)

    active = next_active.copy()

print(len(active))
