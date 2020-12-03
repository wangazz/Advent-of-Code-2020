import os
input_path = '../Inputs/Day-3.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

tree_counter_1 = 0
position = 0
width = len(inputs[0])

# Part 1: Right 3, down 1

for i in inputs:
    position = position % width
    if i[position] == '#':
        tree_counter_1 += 1
    position += 3

print(tree_counter_1)

# Part 2
# Right 1, down 1
tree_counter_2 = 0
position = 0
for i in inputs:
    position = position % width
    if i[position] == '#':
        tree_counter_2 += 1
    position += 1

# Right 5, down 1
tree_counter_3 = 0
position = 0
for i in inputs:
    position = position % width
    if i[position] == '#':
        tree_counter_3 += 1
    position += 5

# Right 7, down 1
tree_counter_4 = 0
position = 0
for i in inputs:
    position = position % width
    if i[position] == '#':
        tree_counter_4 += 1
    position += 7

# Right 1, down 2
tree_counter_5 = 0
position = 0
for index in range(len(inputs)):
    if index % 2 == 0:
        i = inputs[index]
        position = position % width
        if i[position] == '#':
            tree_counter_5 += 1
        position += 1

print(tree_counter_1 * tree_counter_2 * tree_counter_3 * tree_counter_4 * tree_counter_5)
