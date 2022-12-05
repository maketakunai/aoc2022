#!/usr/bin/env python3

def get_val(inp):
    if inp == 'X':
        return 1
    if inp == 'Y':
        return 2
    if inp == 'Z':
        return 3

with open('./input/02_input.txt') as input_file:
    total = 0
    win = {'A':'Y', 'B':'Z', 'C':'X'}
    lose = {'A':'Z', 'B':'X', 'C':'Y'}
    draw = {'A':'X', 'B':'Y', 'C':'Z'}
    for i in input_file.read().splitlines():
        a = i.split(' ')

        if a[1] == 'X':
            b = lose[a[0]]
            total += get_val(b) + 0
        elif a[1] == 'Y':
            b = draw[a[0]]
            total += get_val(b) + 3
        else:
            b = win[a[0]]
            total += get_val(b) + 6

    print(total)