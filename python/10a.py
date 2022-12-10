#!/usr/bin/env python3

with open('./input/10_input.txt') as input_file:
    x = 1
    cycle = 0
    sig_str = []
    to_record = [20,60,100,140,180,220]

    for line in input_file.read().splitlines():
        instruction = line.split(' ')
        match instruction[0]:
            case 'noop':
                cycle += 1
                if cycle in to_record:
                    sig_str.append(cycle*x)
            case 'addx':
                flag = 0
                counter = 2
                while counter != 0:
                    cycle += 1
                    counter -= 1
                    if cycle in to_record:
                        sig_str.append(cycle*x)
                        flag = 1
                if flag == 0:
                    if cycle in to_record:
                        sig_str.append(cycle*x)
                x += int(instruction[1])
                
    print(sum(sig_str))


# if cycle in to_record:
#     sig_str.append(cycle*x)