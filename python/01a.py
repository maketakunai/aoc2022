#!/usr/bin/env python3

with open('./input/01_input.txt') as input_file:
    big = 0
    temp = 0
    for i in input_file.read().splitlines():
        if i != '':
            temp += int(i)
        else:
            if temp > big:
                big = temp
            temp = 0
    
    print(big)
