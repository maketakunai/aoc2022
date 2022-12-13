#!/usr/bin/env python3
import ast,functools

def compare(a,b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0
    if isinstance(a, int):
        a = [a]
        return compare(a,b)
    elif isinstance(b, int):
        b = [b]
        return compare(a,b)
    for a_,b_ in zip(a,b):
        res = compare(a_,b_)
        if res:
            return res
    return compare(len(a), len(b))

with open('./input/13_input.txt') as input_file:
    packets = [line for line in input_file.read().splitlines()]
    packets = [ast.literal_eval(i) for i in packets if i]
    packets.extend( [[[2]],[[6]]])
    
    sorted_packet = sorted(packets, key=functools.cmp_to_key(compare))
    
    target = (sorted_packet.index([[2]])+1) * (sorted_packet.index([[6]])+1)
    print(target)