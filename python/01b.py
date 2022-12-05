#!/usr/bin/env python3

with open('./input/01_input.txt') as input_file:
    cals = []
    temp = 0
    for i in input_file.read().splitlines():
        if i != '':
            temp += int(i)
        else:
            cals.append(temp)
            temp = 0
    print(sum(sorted(cals)[-3:]))
    
