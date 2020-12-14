import os
import re

input_path = '../Inputs/Day-14.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

bits = 36

# Part 1
mask = str()
memory = []

for line in inputs:
    if line[:4] == 'mask':
        mask = re.findall('mask = (.{36})', line)[0]
    elif line[:3] == 'mem':
        pattern = re.findall('mem\[(\d+)\] = (\d+)', line)
        address, value = map(int, pattern[0])
        value_to_bin = bin(value)
        binary = '0' * (bits - len(value_to_bin) + 2) + value_to_bin[2:]

        for index, bit in enumerate(mask):
            if bit != 'X':
                binary = binary[:index] + bit + binary[index + 1:]

        memory = [m for m in memory if m[0] != address]
        memory.append((address, int(binary, base=2)))
    else:
        raise Exception()

print(sum([m[1] for m in memory]))
