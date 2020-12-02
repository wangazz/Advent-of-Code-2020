import os
input_path = '../Inputs/Day-2.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

valid_count_part_1 = 0
valid_count_part_2 = 0

for i in inputs:
    split_string = i.split(': ')
    bounds = split_string[0].split('-')
    lower_bound = int(bounds[0])
    bounds_split = bounds[1].split(' ')
    upper_bound = int(bounds_split[0])

    test_char = bounds_split[1]
    password_to_test = split_string[1]

    occurences = password_to_test.count(test_char)
    if occurences >= lower_bound and occurences <= upper_bound:
        valid_count_part_1 += 1

    if (password_to_test[lower_bound - 1] == test_char) is not (password_to_test[upper_bound - 1] == test_char):
        valid_count_part_2 += 1

print(valid_count_part_1)
print(valid_count_part_2)
