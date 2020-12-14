import itertools
import os
import re

input_path = '../Inputs/Day-14.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

bits = 36

# Part 1
mask = ''
memory = []

for line in inputs:
    if line[:4] == 'mask':
        mask = re.findall('mask = (.{36})', line)[0]
    elif line[:3] == 'mem':
        pattern = re.findall('mem\[(\d+)\] = (\d+)', line)
        address, value = map(int, pattern[0])
        value_to_bin = bin(value)
        binary_val = '0' * (bits - len(value_to_bin) + 2) + value_to_bin[2:]

        for index, bit in enumerate(mask):
            if bit != 'X':
                binary_val = binary_val[:index] + bit + binary_val[index + 1:]

        memory = [m for m in memory if m[0] != address]
        memory.append((address, int(binary_val, base=2)))
    else:
        raise Exception()

print(sum([m[1] for m in memory]))

# Part 2
mask = ''
memory = []

for line in inputs:
    if line[:4] == 'mask':
        mask = re.findall('mask = (.{36})', line)[0]
    elif line[:3] == 'mem':
        pattern = re.findall('mem\[(\d+)\] = (\d+)', line)
        address, value = map(int, pattern[0])
        address_to_bin = bin(address)
        binary_addr = '0' * (bits - len(address_to_bin) + 2) + address_to_bin[2:]

        for index, bit in enumerate(mask):
            if bit == '1' or bit == 'X':
                binary_addr = binary_addr[:index] + bit + binary_addr[index + 1:]

        all_addr = [binary_addr]

        while any('X' in a for a in all_addr):
            for a in all_addr:
                if 'X' in a:
                    all_addr.remove(a)
                    x_index = a.index('X')
                    all_addr.append(a[:x_index] + '0' + a[x_index + 1:])
                    all_addr.append(a[:x_index] + '1' + a[x_index + 1:])

        for a in all_addr:
            int_addr = int(a, base=2)
            memory = [m for m in memory if m[0] != int_addr]
            memory.append((int_addr, value))
    else:
        raise Exception()

print(sum([m[1] for m in memory]))
