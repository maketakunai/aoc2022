#!/usr/bin/env python3

def sum_file_sizes(dir):
    return sum([n[1] for n in dir])

with open('./input/07_input.txt') as input_file:
    cur_dir = []
    files = {}
    for line in input_file.read().splitlines():
        if line[0] == '$':
            command = line.split(' ')
            if command[1] == 'cd' and command[2] != '..':
                cur_dir.append(command[2])
            elif command[1] == 'cd' and command[2] == '..':
                cur_dir.pop() 
        else:
            ls_result = line.split(' ')
            if ls_result[0] != 'dir':
                f_size = int(ls_result[0])
                for n in range(len(cur_dir)):
                    if tuple(cur_dir[:n+1]) not in files:
                        files[tuple(cur_dir[:n+1])] = f_size
                    else:
                        files[tuple(cur_dir[:n+1])] += f_size


    total = sum(file_size for file_size in files.values() if file_size <= 100000)
    print(total)
