import os
input_path = '../Inputs/Day-5.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

seat_ids = []

for i in inputs:
    rows = i[:7]
    columns = i[7:10]

    all_rows = list(range(128))
    all_columns = list(range(8))

    for r in rows:
        if r == 'F':
            all_rows = all_rows[:int(len(all_rows) / 2)]
        elif r == 'B':
            all_rows = all_rows[int(len(all_rows) / 2):]

    for c in columns:
        if c == 'L':
            all_columns = all_columns[:int(len(all_columns) / 2)]
        elif c == 'R':
            all_columns = all_columns[int(len(all_columns) / 2):]

    id = all_rows[0] * 8 + all_columns[0]
    seat_ids.append(id)

print(max(seat_ids))

all_seat_ids = []
for i in range(128):
    for j in range(8):
        all_seat_ids.append(i * 8 + j)

for id in all_seat_ids:
    if id not in seat_ids:
        if id - 1 in seat_ids and id + 1 in seat_ids:
            print(id)
