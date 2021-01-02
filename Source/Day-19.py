import os
import re

input_path = '../Inputs/Day-19.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

rules = {}
messages = []

for line in inputs:
    if pattern := re.findall('(\d+): (.+)', line):
        rule_id = int(pattern[0][0])
        rule = pattern[0][1]
        rules.update({rule_id: rule})
    elif line != '':
        messages.append(line)

1