import os
import re
input_path = '../Inputs/Day-7.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

# Part 1
bags = []
contents = []

for i in inputs:
    patterns = re.findall('^(.*) bags contain (.*)\.$', i)
    outer = patterns[0][0]
    inner = patterns[0][1]
    if outer != 'shiny gold' and inner != 'no other bags':
        inner_bags = inner.split(', ')
        inner_bags_list = []
        for bag in inner_bags:
            patterns = re.findall('^\d+ (.*) bags?$', bag)
            inner_bags_list.append(patterns[0])

        bags.append(outer)
        contents.append(inner_bags_list)

while True:
    new_contents = []
    for c in contents:
        x = []
        for bag in c:
            if bag in bags:
                inner_bags = contents[bags.index(bag)]
                x.extend(inner_bags)
            else:
                x.append(bag)
        new_contents.append(x)
    if contents == new_contents:
        break
    else:
        contents = new_contents

shiny_gold_counter = 0
for c in contents:
    if 'shiny gold' in c:
        shiny_gold_counter += 1

print(shiny_gold_counter)

# Part 2
bags = []
contents = []

for i in inputs:
    patterns = re.findall('^(.*) bags contain (.*)\.$', i)
    outer = patterns[0][0]
    inner = patterns[0][1]
    if inner != 'no other bags':
        inner_bags = inner.split(', ')
        inner_bags_list = []
        for bag in inner_bags:
            patterns = re.findall('^(\d+) (.*) bags?$', bag)
            inner_bags_list.append((int(patterns[0][0]), patterns[0][1]))

        bags.append(outer)
        contents.append(inner_bags_list)

bag_counter = -1 # ignore the shiny gold bag
target_contents = [(1, 'shiny gold')]
new_target_contents = []

while True:
    new_target_contents = []
    for c in target_contents:
        multiplier = c[0]
        target = c[1]

        bag_counter += multiplier

        if target in bags:
            new_target_contents.extend([(c[0] * multiplier, c[1]) for c in contents[bags.index(target)]])

    if new_target_contents == target_contents:
        break
    else:
        target_contents = new_target_contents

print(bag_counter)
