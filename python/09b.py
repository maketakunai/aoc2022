#!/usr/bin/env python3
import math

def distance(x_h,y_h,x_t,y_t):
    dist = math.sqrt((x_h - x_t)**2+(y_h - y_t)**2)
    return dist > math.sqrt(2)

def move_body(prev, curr):
    temp = curr
    if distance(prev[0],prev[1],curr[0],curr[1]):
        if prev[0] > curr[0]:
            temp[0]+=1
        elif prev[0] < curr[0]:
            temp[0]-=1
        if prev[1] > curr[1]:
            temp[1]+=1
        elif prev[1] < curr[1]:
            temp[1]-=1
        
        return temp
    else:
        return curr

with open('./input/09_input.txt') as input_file:

    tail_visited = set()
    snek = [[0,0] for _ in range(9)]
    head = [0,0]
    for line in input_file.read().splitlines():
        direction,steps = line.split(' ')
        for i in range(1,int(steps)+1):
            match direction:
                case 'R':
                    head[0] += 1
                case 'L':
                    head[0] -= 1
                case 'U':
                    head[1] += 1
                case 'D':
                    head[1] -= 1
            prev = head
            for index, curr in enumerate(snek):
                snek[index] = move_body(prev, curr)
                prev = snek[index]

            tail_visited.add(tuple(snek[-1]))
        
    print(len(tail_visited))