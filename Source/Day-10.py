import os
input_path = '../Inputs/Day-10.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [int(line.strip()) for line in f]

inputs.sort()
max_difference = 3
device = max(inputs) + max_difference

# Part 1
all_inputs = [0, *inputs, device]
input_length = len(all_inputs)
differences = [all_inputs[i + 1] - all_inputs[i] for i in range(input_length - 1)]
distribution = differences.count(1) * differences.count(3)
print(distribution)

# Part 2
# If the difference between two values is 3, we must keep both values
keep = [[0], *[[all_inputs[i], all_inputs[i + 1]] for i in range(len(differences)) if differences[i] == max_difference], [device]]
flatten_keep = [i for l in keep for i in l]
indices_to_keep = sorted(set([all_inputs.index(k) for k in flatten_keep]))

def maxGap(differences):
    gap = 0
    gaps = []
    for d in differences:
        if d != 3:
            gap += 1
        else:
            gaps.append(gap)
            gap = 0
    return max(gaps)

# There are no gaps of 2 and the max consecutive gaps of 1 is 4
# So, there can be 0, 1, 2 or 3 intermediate values between pairs of values with difference 3
# If 0: pass
# If 1: 2 valid states (present or not present)
# If 2: 4 valid states (any combination of present or not present)
# If 3: 7 valid states (any combination of present or not present, such that at least 1 is present)

valid_states = 1

for i in range(len(indices_to_keep) - 1):
    start = indices_to_keep[i]
    end = indices_to_keep[i + 1]
    input_slice = all_inputs[start:end]
    intermediate_values = len(input_slice) - 1
    if intermediate_values == 1:
        valid_states *= 2
    elif intermediate_values == 2:
        valid_states *= 4
    elif intermediate_values == 3:
        valid_states *= 7

print(valid_states)
