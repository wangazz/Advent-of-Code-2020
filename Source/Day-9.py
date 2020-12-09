import os
input_path = '../Inputs/Day-9.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [int(line.strip()) for line in f]

preamble_length = 25

# Part 1

i = preamble_length
invalid_number = int()

while i < len(inputs):
    preamble = inputs[i - preamble_length:i]
    valid_data = set([i + j for i in preamble for j in preamble if i != j])

    number = inputs[i]

    if number not in valid_data:
        invalid_number = number
        break

    i += 1

print(invalid_number)

# Part 2

sequences = []
for start in range(preamble_length, len(inputs) - 2):
    for end in range(preamble_length + 1, len(inputs) - 1):
        if start < end - 1:
            sequence = inputs[start:end]
            sequences.append(sequence)

for s in sequences:
    if sum(s) == invalid_number:
        print(min(s) + max(s))
        break
