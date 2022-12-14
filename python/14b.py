#!/usr/bin/env python3

def drop_grain(x,y,lines,grains):
    while True:
        down_coord = (x, y+1)
        left_down_diag = (x-1, y+1)
        right_down_diag = (x+1, y+1)
        if down_coord not in lines and down_coord not in grains:
            y = y+1
        elif left_down_diag not in lines and left_down_diag not in grains:
            x,y = x-1, y+1
        elif right_down_diag not in lines and right_down_diag not in grains:
            x,y = x+1, y+1
        else:
            if x == 500 and y == 0:
                return None
            else:
                return [x,y]
        
with open('./input/14_input.txt') as input_file:
    lines = set()
    grains = set()

    for line in input_file.read().splitlines():
        segments = line.split(' -> ')
        for s in range(len(segments)-1):
            x1,y1 = [int(i) for i in segments[s].split(',')]
            x2,y2 = [int(i) for i in segments[s+1].split(',')]
            if x1 == x2:
                for new_y in range(min(y1,y2),max(y1,y2)+1):
                    lines.add((x1,new_y))
            elif y1 == y2:
                for new_x in range(min(x1,x2),max(x1,x2)+1):
                    lines.add((new_x,y1))

    xs = [x for x,y in list(lines)]
    ys = [y for x,y in list(lines)]
    x_min = min(xs)
    x_max = max(xs)
    y_min = min(ys)
    y_max = max(ys)
    bottom_bar = [(a,y_max+2) for a in range(x_min-1000,x_max+1000)]
    for x in bottom_bar:
        lines.add(x)
    new_ymax = max([y for x,y in list(lines)])

    while True:
        result = drop_grain(500,0,lines,grains)
        if result is None:
            break
        grains.add((result[0],result[1]))

    
    print(len(grains)+1)
  



