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
            inner_bags_list.append(patterns[0][1])

        bags.append(outer)
        contents.append(inner_bags_list)

while(True):
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
            inner_bags_list.append((patterns[0][0], patterns[0][1]))

        bags.append(outer)
        contents.append(inner_bags_list)

while(True):
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

shiny_gold_contents = contents[bags.index('shiny gold')]
distinct_contents = set(shiny_gold_contents)
print(len(distinct_contents))
