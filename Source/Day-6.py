import numpy as np
import os
import re
input_path = '../Inputs/Day-6.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

# Part 1
groups = []
group = ''
for i in inputs:
    if i != '':
        group += i
    else:
        groups.append(group)
        group = ''

distinct = []
for group in groups:
    values, counts = np.unique(list(group), return_counts=True)
    distinct.append(len(counts))

print(sum(distinct))

# Part 2
groups = []
group = []
for i in inputs:
    if i != '':
        group.append(list(i))
    else:
        groups.append(group)
        group = []

distinct = []
for group in groups:
    intersect = set.intersection(*[set(x) for x in group])
    distinct.append(len(intersect))

print(sum(distinct))
