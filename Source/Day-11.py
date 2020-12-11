import os
input_path = '../Inputs/Day-11.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

rows = len(inputs)
columns = len(inputs[0])

# Part 1
while True:
    new_map = []
    for row in range(rows):
        new_row = ''
        for column in range(columns):
            seat = inputs[row][column]

            if seat == '.':
                new_row += seat
            else:
                adjacent = [inputs[i][j] for i in [row - 1, row, row + 1] for j in [column - 1, column, column + 1] if i >= 0 and j >= 0 and i < rows and j < columns and not (i == row and j == column)]
                occupied = adjacent.count('#')

                if seat == 'L' and occupied == 0:
                    new_row += '#'
                elif seat == '#' and occupied >= 4:
                    new_row += 'L'
                else:
                    new_row += seat

        new_map.append(new_row)
    if new_map == inputs:
        break
    else:
        inputs = new_map

occupied_count = 0
for i in new_map:
    occupied_count += i.count('#')
print(occupied_count)

# Part 2
def first(list):
    if len(list) == 0:
        return 'n/a'
    else:
        return list[0]

while True:
    new_map = []
    for row in range(rows):
        new_row = ''
        for column in range(columns):
            seat = inputs[row][column]

            if seat == '.':
                new_row += seat
            else:
                n = [inputs[row - i][column] for i in range(1, row + 1) if inputs[row - i][column] != '.']
                s = [inputs[row + i][column] for i in range(1, rows - row) if inputs[row + i][column] != '.']
                w = [inputs[row][column - i] for i in range(1, column + 1) if inputs[row][column - i] != '.']
                e = [inputs[row][column + i] for i in range(1, columns - column) if inputs[row][column + i] != '.']
                nw = [inputs[row - i][column - i] for i in range(1, min(row, column) + 1) if inputs[row - i][column - i] != '.']
                ne = [inputs[row - i][column + i] for i in range(1, min(row + 1, columns - column)) if inputs[row - i][column + i] != '.']
                sw = [inputs[row + i][column - i] for i in range(1, min(rows - row, column + 1)) if inputs[row + i][column - i] != '.']
                se = [inputs[row + i][column + i] for i in range(1, min(rows - row, columns - column)) if inputs[row + i][column + i] != '.']

                search = [n, ne, e, se, s, sw, w, nw]
                adjacent = list(map(first, search))
                occupied = adjacent.count('#')

                if seat == 'L' and occupied == 0:
                    new_row += '#'
                elif seat == '#' and occupied >= 5:
                    new_row += 'L'
                else:
                    new_row += seat

        new_map.append(new_row)
    if new_map == inputs:
        break
    else:
        inputs = new_map

occupied_count = 0
for i in new_map:
    occupied_count += i.count('#')
print(occupied_count)
