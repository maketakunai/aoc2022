#!/usr/bin/env python3

with open('./input/03_input.txt') as input_file:
    alphabet = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,53)))
    sum = 0
    lines = [line.rstrip() for line in input_file]
    for l in range(0, len(lines), 3):
        chunk = lines[l:l+3]
        a = set(list(chunk[0]))
        b = set(list(chunk[1]))
        c = set(list(chunk[2]))
        temp = a&b&c
        x = temp.pop()
        sum += alphabet[x]

    print(sum)