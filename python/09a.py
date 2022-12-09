#!/usr/bin/env python3
import math
def distance(x_h,y_h,x_t,y_t):
    dist = math.sqrt((x_h - x_t)**2+(y_h - y_t)**2)
    return dist > math.sqrt(2)

with open('./input/09_input.txt') as input_file:
    head_visited = set()
    tail_visited = set()
    x_h, y_h = 0,0
    x_t, y_t = 0,0
    for line in input_file.read().splitlines():
        direction,steps = line.split(' ')
        for i in range(1,int(steps)+1):
            match direction:
                case 'R':
                    x_h += 1
                    if distance(x_h,y_h,x_t,y_t):
                        x_t = x_h - 1
                        y_t = y_h
                case 'L':
                    x_h -= 1
                    if distance(x_h,y_h,x_t,y_t):
                        x_t = x_h + 1
                        y_t = y_h
                case 'U':
                    y_h += 1
                    if distance(x_h,y_h,x_t,y_t):
                        x_t = x_h 
                        y_t = y_h - 1
                case 'D':
                    y_h -= 1
                    if distance(x_h,y_h,x_t,y_t):
                        x_t = x_h 
                        y_t = y_h + 1

            head_visited.add((x_h,y_h))
            tail_visited.add((x_t,y_t))
        
    print(len(tail_visited))