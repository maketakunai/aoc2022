#!/usr/bin/env python3

with open('./input/06_input.txt') as input_file:
    for line in input_file.read().splitlines():
        for c in range(0, len(line)-4):
            temp = set([*line[c:c+4]])
            if len(temp) == 4:
                print(c+4)
                break