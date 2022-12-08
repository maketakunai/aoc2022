#!/usr/bin/env python3

def check_distance(target,trees):
    counter = 0
    for tree in trees:
        if target > tree:
            counter +=1
        else:
            return (counter + 1)
    return counter


def is_clear_path(grid,y,x):
    row = grid[y]
    left_row = row[x+1:]
    target_num = grid[y][x]
    right_row = reversed(row[:x])
    col = [r[x] for r in grid]
    col_below = col[y+1:]
    col_above = reversed(col[:y])
    num = check_distance(target_num, left_row) * check_distance(target_num, right_row) * check_distance(target_num, col_below) * check_distance(target_num, col_above)
    return num

with open('./input/08_input.txt') as input_file:
    large = 0
    grid = [[*line] for line in input_file.read().splitlines()]
    for y in range(1,len(grid)-1):
        for x in range(1, len(grid[0])-1):
            product = is_clear_path(grid,y,x)
            if (product > large):
                large = product

    print(large)
