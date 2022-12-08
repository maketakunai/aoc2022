#!/usr/bin/env python3

def is_clear_path(grid,y,x):
    row = grid[y]
    left_row = row[x+1:]
    target_num = grid[y][x]
    right_row = row[:x]
    row_check1 = all(target_num > n for n in right_row)
    row_check2 = all(target_num > n for n in left_row)
    col = [r[x] for r in grid]
    col_below = col[y+1:]
    col_above = col[:y]
    col_check1 = all(target_num > n for n in col_above)
    col_check2 = all(target_num > n for n in col_below)
    return (row_check1 or row_check2 or col_check1 or col_check2)

with open('./input/08_input.txt') as input_file:
    visible = 0
    grid = [[*line] for line in input_file.read().splitlines()]
    for y in range(1,len(grid)-1):
        for x in range(1, len(grid[0])-1):
           if (is_clear_path(grid,y,x)):
            visible += 1
    
    visible += len(grid)*2 + len(grid[0])*2 - 4
    print(visible)