#!/usr/bin/env python3
import ast

def compare(a,b):
    if isinstance(a, int) and isinstance(b, int):
        if a == b:
            return -1
        return a < b
    elif isinstance(a, int):
        a = [a]
    elif isinstance(b, int):
        b = [b]
    for a_,b_ in zip(a,b):
        res = compare(a_,b_)
        if res != -1:
            return res
    if len(a) < len(b):
        return True
    elif len(a) > len(b):
        return False
    return -1

        

with open('./input/13_input.txt') as input_file:
    packets = [line for line in input_file.read().splitlines()]
    counter, total = 0, 0
    for n in range(0,len(packets),3):
        counter += 1
        a,b = ast.literal_eval(packets[n]), ast.literal_eval(packets[n+1])
        if compare(a,b):
            total += counter
    print(total)