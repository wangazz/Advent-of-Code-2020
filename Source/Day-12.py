import os
input_path = '../Inputs/Day-12.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [(line.strip()[0], int(line.strip()[1:])) for line in f]

# Part 1
directions = ['N', 'E', 'S', 'W']
dir_index = 1
x = 0
y = 0

for inst, arg in inputs:
    if inst == 'L':
        dir_index -= int(arg / 90)
        dir_index = dir_index % 4
    elif inst == 'R':
        dir_index += int(arg / 90)
        dir_index = dir_index % 4
    elif inst == 'F':
        inst = directions[dir_index]

    if inst == 'N':
        y += arg
    elif inst == 'E':
        x += arg
    elif inst == 'S':
        y -= arg
    elif inst == 'W':
        x -= arg

print(abs(x) + abs(y))

# Part 2
x = 0
y = 0
waypoint_x = 10
waypoint_y = 1

for inst, arg in inputs:
    if inst == 'L':
        transforms = int(arg / 90)
        for t in range(transforms):
            new_waypoint_y = waypoint_x
            new_waypoint_x = -waypoint_y
            waypoint_x = new_waypoint_x
            waypoint_y = new_waypoint_y
    elif inst == 'R':
        transforms = int(arg / 90)
        for t in range(transforms):
            new_waypoint_x = waypoint_y
            new_waypoint_y = -waypoint_x
            waypoint_x = new_waypoint_x
            waypoint_y = new_waypoint_y
    elif inst == 'F':
        x += waypoint_x * arg
        y += waypoint_y * arg

    if inst == 'N':
        waypoint_y += arg
    elif inst == 'E':
        waypoint_x += arg
    elif inst == 'S':
        waypoint_y -= arg
    elif inst == 'W':
        waypoint_x -= arg

print(abs(x) + abs(y))
