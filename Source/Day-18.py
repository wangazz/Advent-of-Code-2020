import os
import re

input_path = '../Inputs/Day-18.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

def evaluate(expression: str):
    result = 0
    operator = '+'
    term = ''
    for i, char in enumerate(expression):
        if re.match('\d', char):
            term += char
            if i != len(expression) - 1 and re.match('\d', expression[i+1]):
                pass
            elif operator == '+':
                result += int(term)
                term = ''
            elif operator == '*':
                result *= int(term)
                term = ''
        elif re.match('\+|\*', char):
            operator = char
    return result

# Part 1
running_count = 0
for line in inputs:
    line = line.replace(' ', '')
    start_index, end_index = 0, 0
    while '(' in line:
        # Find the rightmost '(' to the left of a ')'
        for i, char in enumerate(line):
            if char == '(':
                start_index = i
            elif char == ')':
                end_index = i
                break

        # Evaluate the expression
        expression = line[start_index + 1:end_index]
        result = evaluate(expression)

        # Replace the bracketed string
        line = line[:start_index] + str(result) + line[end_index + 1:]

    assert '(' not in line and ')' not in line
    running_count += evaluate(line)

print(running_count)

# Part 2
def evaluate_advanced(expression: str):
    while '+' in expression:
        add_terms = re.findall('(\d+)\+(\d+)', expression)
        left, right = add_terms[0]
        add_result = int(left) + int(right)
        expression = expression.replace(f'{left}+{right}', str(add_result), 1)
    return evaluate(expression)

advanced_count = 0
for line in inputs:
    line = line.replace(' ', '')
    start_index, end_index = 0, 0
    while '(' in line:
        for i, char in enumerate(line):
            if char == '(':
                start_index = i
            elif char == ')':
                end_index = i
                break

        expression = line[start_index + 1:end_index]
        result = evaluate_advanced(expression)

        line = line[:start_index] + str(result) + line[end_index + 1:]

    assert '(' not in line and ')' not in line
    advanced_count += evaluate_advanced(line)

print(advanced_count)
