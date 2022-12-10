#!/usr/bin/env python3

with open('./input/10_input.txt') as input_file:
    x = 1
    cycle = 0
    screen = []

    for line in input_file.read().splitlines():
        instruction = line.split(' ')
        match instruction[0]:
            case 'noop':
                if cycle % 40 in [x-1, x, x+1]:
                    screen.append('#')
                else:
                    screen.append('.')
                cycle += 1
            case 'addx':
                for _ in range(2):
                    if cycle % 40 in [x-1, x, x+1]:
                        screen.append('#')
                    else:
                        screen.append('.')
                    cycle += 1
                x += int(instruction[1])

    display = [screen[i:i+40] for i in range(0, len(screen),40)]
    for n in display:
        print(''.join(n))