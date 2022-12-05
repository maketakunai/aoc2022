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
    win = [['A','Y'], ['B', 'Z'], ['C', 'X']]
    lose = [['A', 'Z'], ['B', 'X'], ['C', 'Y']]
    for i in input_file.read().splitlines():
        a = i.split(' ')
        if a in win:
            total += get_val(a[1]) + 6
        elif a in lose:
            total += get_val(a[1]) + 0
        else:
            total += get_val(a[1]) + 3
    print(total)