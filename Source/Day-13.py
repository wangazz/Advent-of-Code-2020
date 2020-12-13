import os
from sympy.ntheory.modular import crt

input_path = '../Inputs/Day-13.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

ids = [int(id) for id in inputs[1].split(',') if id != 'x']

# Part 1
timestamp = int(inputs[0])
departures = [(id, id - (timestamp % id)) for id in ids]
departures.sort(key=lambda d: d[1])
print(departures[0][0] * departures[0][1])

# Part 2
all_ids = [0 if id == 'x' else int(id) for id in inputs[1].split(',')]
offsets = [-all_ids.index(id) for id in ids]

print(crt(ids, offsets)[0])
