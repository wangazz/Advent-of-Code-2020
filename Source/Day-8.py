import os
input_path = '../Inputs/Day-8.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

# Part 1
accumulator = 0
executed = []
i = 0

while i not in executed:
    executed.append(i)
    split = inputs[i].split(' ')
    inst = split[0]
    arg = int(split[1])

    if inst == 'nop':
        i += 1
    elif inst == 'acc':
        accumulator += arg
        i += 1
    elif inst == 'jmp':
        i = i + arg

print(accumulator)

# Part 2
possible_inputs = []
for i in range(len(inputs)):
    split = inputs[i].split(' ')
    inst = split[0]
    arg = int(split[1])

    if inst == 'jmp':
        possible_input = ['nop ' + str(arg) if index == i else inputs[index] for index in range(len(inputs))]
        possible_inputs.append(possible_input)
    elif inst == 'nop':
        possible_input = ['jmp ' + str(arg) if index == i else inputs[index] for index in range(len(inputs))]
        possible_inputs.append(possible_input)

for input in possible_inputs:
    accumulator = 0
    executed = []
    i = 0

    while i not in executed:
        executed.append(i)
        split = input[i].split(' ')
        inst = split[0]
        arg = int(split[1])

        if inst == 'nop':
            i += 1
        elif inst == 'acc':
            accumulator += arg
            i += 1
        elif inst == 'jmp':
            i = i + arg
        
        if i == len(inputs):
            print(accumulator)
            break
