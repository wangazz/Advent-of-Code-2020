import os
input_path = '../Inputs/Day-1.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [int(line.strip()) for line in f]
inputs_length = len(inputs)

for i in range(inputs_length):
    for j in range(inputs_length):
        if inputs[i] + inputs[j] == 2020:
            print(inputs[i] * inputs[j])

for i in range(inputs_length):
    for j in range(inputs_length):
        for k in range(inputs_length):
            if inputs[i] + inputs[j] + inputs[k] == 2020:
                print(inputs[i] * inputs[j] * inputs[k])
