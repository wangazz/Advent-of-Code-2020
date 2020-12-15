import os
input_path = '../Inputs/Day-15.txt'
# input_path = '../Inputs/Test.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

# Part 1
# numbers = [int(i) for i in inputs[0].split(',')]
# numbers.reverse()

# i = len(numbers)
# while i < 2020:
#     last = numbers[0]
#     next_number = int()
#     if numbers.count(last) == 1:
#         next_number = 0
#     else:
#         second_last = numbers[1:].index(last)
#         next_number = second_last + 1
#     numbers.insert(0, next_number)
#     i += 1

# print(numbers[0])

# Part 2
numbers = [int(i) for i in inputs[0].split(',')]
history = dict(zip(numbers[:len(numbers)], range(len(numbers))))
last = numbers[-1]

i = len(numbers)
while i < 30000000:
    next_val = i - 1 - history.get(last, i - 1)
    history.update({last: i - 1})
    last = next_val

    i += 1

print(last)
