#!/usr/bin/env python3
import re
# crates = { 
# 1:['Z','N'],
# 2:['M','C','D'],
# 3:['P'],
# }
crates = { 
1:['B','Q','C'],
2:['R','Q','W','Z'],
3:['B','M','R','L','V'],
4:['C','Z','H','V','T','W'],
5:['D','Z','H','B','N','V','G'],
6:['H','N','P','C','J','F','V','Q'],
7:['D','G','T','R','W','Z','S'],
8:['C','G','M','N','B','W','Z','P'],
9:['N','J','B','M','W','Q','F','P']
}

with open('./input/05_input.txt') as input_file:
    answer = ''
    input = input_file.read().splitlines()
    directions = input[10:]
    for dir in directions:
        s_dirs = re.findall('\d+',dir)
        s_dirs = [int(i) for i in s_dirs]
        how_many = s_dirs[0]

        while how_many > 0:
            temp = crates[s_dirs[1]].pop(-1)
            crates[s_dirs[2]].append(temp)
            how_many -= 1
    for k,v in crates.items():
        answer += v[-1]
    print(answer)