import os
import re
# import statistics

input_path = '../Inputs/Day-16.txt'
# input_path = '../Inputs/Test.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

fields = []
valid_ranges = []
assert len(fields) == len(valid_ranges)
for line in inputs:
    if pattern := re.findall('(.+): (\d+)-(\d+) or (\d+)-(\d+)', line):
        field, lower1, upper1, lower2, upper2 = pattern[0]
        fields.append(field)
        valid_ranges += [range(int(lower1), int(upper1) + 1), range(int(lower2), int(upper2) + 1)]

nearby_tickets = []
reached_nearby_tickets = False
for line in inputs:
    if line == 'nearby tickets:':
        reached_nearby_tickets = True
    elif reached_nearby_tickets == True:
        nearby_tickets.append(line.split(','))

# Part 1
# scanning_error = 0
# for t in nearby_tickets:
#     out_of_range = [int(f) if not any([int(f) in r for r in valid_ranges]) else 0 for f in t]
#     scanning_error += sum(out_of_range)

# print(scanning_error)

# Part 2
for t in nearby_tickets:
    out_of_range = [int(f) if not any([int(f) in r for r in valid_ranges]) else 0 for f in t]
    if sum(out_of_range) > 0:
        nearby_tickets.remove(t)

my_ticket = []
reached_my_ticket = False
for line in inputs:
    if line == 'your ticket:':
        reached_my_ticket = True
    elif reached_my_ticket == True:
        my_ticket.append(line.split(','))
        break
assert len(*my_ticket) == len(fields)

all_tickets = my_ticket + nearby_tickets

computed_fields = []
for i in range(len(*my_ticket)):
    column_field_test = []
    column = [int(t[i]) for t in all_tickets]

    in_range = []
    for r, f in enumerate(fields):
        if all([c in valid_ranges[r * 2] or c in valid_ranges[r * 2 + 1] for c in column]):
            in_range.append(f)

    computed_fields.append(in_range)

decided_fields = []
for iterator in range(1000):
    previous_decided_fields = decided_fields
    for i, f in enumerate(computed_fields):
        if len(f) == 1:
            field = f[0]
            decided_fields.append((i, field))
            computed_fields.remove(f)
            [cf.remove(field) for cf in computed_fields if field in cf]
# cf.remove(f[0]) if f[0] in cf else
print(computed_fields)
print(decided_fields)
