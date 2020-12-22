import os
import re

input_path = '../Inputs/Day-21.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

ingredients = []
allergens = []
for line in inputs:
    match = re.findall('^(.+) \(contains (.+)\)$', line)
    i = match[0][0].split(' ')
    a = match[0][1].split(', ')
    ingredients.append(i)
    allergens.append(a)

all_allergens = set([allergen for item in allergens for allergen in item])

possible_allergens = {}
for a in all_allergens:
    for ingredient, allergen in zip(ingredients, allergens):
        if a in allergen:
            
1