#!/usr/bin/env python3
import collections

with open('./input/12_input.txt') as input_file:
    heightmap = [[*line] for line in input_file.read().splitlines()]
    for y in range(len(heightmap)):
        for x in range(len(heightmap[0])):
            if heightmap[y][x] == 'S':
                start = (y,x)
                heightmap[y][x] = ord('a')-ord('a')
            elif heightmap[y][x] == 'E':
                target_coords = (y,x)
                heightmap[y][x] = ord('z')-ord('a')
            else:
                heightmap[y][x] = ord(heightmap[y][x])-ord('a')

    row = len(heightmap)
    col = len(heightmap[0])

    visited = [[0] * col for _ in range(row)]

    queue = collections.deque()
    queue.append(start)

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    while queue:
        y, x = queue.popleft()
        for dy, dx in directions:
            new_y, new_x = y + dy, x + dx
            if (new_y in range(row)) and (new_x in range(col)) and (visited[new_y][new_x] == 0) and (heightmap[new_y][new_x] <= heightmap[y][x] + 1):
                visited[new_y][new_x] = visited[y][x] + 1
                queue.append((new_y, new_x))

    print(visited[target_coords[0]][target_coords[1]])