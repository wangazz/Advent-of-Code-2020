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
import itertools

# If the difference between two values is 3, we must keep both values
keep = [[0], *[[all_inputs[i], all_inputs[i + 1]] for i in range(len(differences)) if differences[i] == max_difference], [device]]
flatten_keep = [i for l in keep for i in l]
indices_to_keep = set([all_inputs.index(k) for k in flatten_keep])
indices_to_arrange = set(range(input_length)).difference(indices_to_keep)

assert len(indices_to_keep) + len(indices_to_arrange) == input_length

def maxDifference(sorted_iterable):
    d = [sorted_iterable[i + 1] - sorted_iterable[i] for i in range(len(sorted_iterable) - 1)]
    return max(d)

counter = 0
arrangement_length = len(indices_to_arrange)
for i in range(int(arrangement_length / 3) - 1, arrangement_length + 1):
    combinations = itertools.combinations(indices_to_arrange, i)
    for c in combinations:
        combined_indices = tuple(indices_to_keep) + c
        candidate_sequence = [all_inputs[index] for index in sorted(combined_indices)]
        if candidate_sequence[0] == 0 and candidate_sequence[-1] == device:
            if maxDifference(candidate_sequence) <= 3:
                counter += 1

print(counter)
