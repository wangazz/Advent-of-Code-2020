import os
import re
input_path = '../Inputs/Day-4.txt'
fp = os.path.join(os.path.dirname(__file__), input_path)

with open(fp, 'r') as f:
    inputs = [line.strip() for line in f]

required_fields = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']

passports = []
passport = ''
for i in inputs:
    if i != '':
        passport += i + ' '
    else:
        passports.append(passport)
        passport = ''

# Part 1
valid_passports = []
valid_count = 0
for p in passports:
    fields_present = 0
    for field in required_fields:
        if field in p:
            fields_present += 1
    if fields_present == len(required_fields):
        valid_count += 1
        valid_passports.append(p)

print(valid_count)

# Part 2
valid_count = 0
for p in valid_passports:
    byr = int(re.findall('byr:(\d+)\s', p)[0])
    byr_valid = byr >= 1920 and byr <= 2002

    iyr = int(re.findall('iyr:(\d+)\s', p)[0])
    iyr_valid = iyr >= 2010 and iyr <= 2020

    eyr = int(re.findall('eyr:(\d+)\s', p)[0])
    eyr_valid = eyr >= 2020 and eyr <= 2030

    hgt = re.findall('hgt:(\d+)(cm|in)', p)
    hgt_valid = False
    if len(hgt) > 0:
        if hgt[0][1] == 'cm' and int(hgt[0][0]) >= 150 and int(hgt[0][0]) <= 193:
            hgt_valid = True
        elif hgt[0][1] == 'in' and int(hgt[0][0]) >= 59 and int(hgt[0][0]) <= 76:
            hgt_valid = True

    ecl = re.findall('ecl:(\w+)\s', p)
    valid_eye_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    ecl_valid = False
    if len(ecl) > 0:
        ecl_valid = ecl[0] in valid_eye_colours

    hcl = re.findall('hcl:#([a-f0-9]{6})\s', p)
    hcl_valid = False
    if len(hcl) > 0:
        hcl_valid = True

    pid = re.findall('pid:(\d{9})\s', p)
    pid_valid = False
    if len(pid) > 0:
        pid_valid = True

    if byr_valid and iyr_valid and eyr_valid and hgt_valid and ecl_valid and hcl_valid and pid_valid:
        valid_count += 1

print(valid_count)
