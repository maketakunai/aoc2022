#!/usr/bin/env python3

with open('./input/06_input.txt') as input_file:
    for line in input_file.read().splitlines():
        for c in range(0, len(line)-14):
            temp = set([*line[c:c+14]])
            if len(temp) == 14:
                print(c+14)
                break