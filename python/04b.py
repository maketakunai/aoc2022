#!/usr/bin/env python3

with open('./input/04_input.txt') as input_file:
    counter = 0
    for line in input_file.read().splitlines():
        p1,p2 = line.split(',')
        r1 = p1.split('-')
        r2 = p2.split('-')
        range1 = [i for i in range(int(r1[0]),int(r1[1])+1)]
        range2 = [i for i in range(int(r2[0]),int(r2[1])+1)]
        check1 = bool(set(range1) & set(range2))
        check2 = bool(set(range2) & set(range1))

        if check1 or check2:
            counter += 1
    print(counter)

        