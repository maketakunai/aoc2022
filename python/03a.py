#!/usr/bin/env python3

with open('./input/03_input.txt') as input_file:
    alphabet = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1,53)))
    sum = 0
    for i in input_file.read().splitlines():
        l = int(len(i) / 2)
        front = set(list(i[:l]))
        back = set(list(i[l:]))
        temp = front & back
        x = temp.pop()
        sum += alphabet[x]
    print(sum)