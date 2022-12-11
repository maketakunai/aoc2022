#!/usr/bin/env python3
from math import lcm

monkey0 = [66, 59, 64, 51]
monkey1 = [67, 61]
monkey2 = [86, 93, 80, 70, 71, 81, 56]
monkey3 = [94]
monkey4 = [71, 92, 64]
monkey5 = [58, 81, 92, 75, 56]
monkey6 = [82, 98, 77, 94, 86, 81]
monkey7 = [54, 95, 70, 93, 88, 93, 63, 50]

worry_ops = [2,7,11,19,3,5,17,13]
lcm_worry = lcm(*worry_ops)

def m0(input):
    counter = 0
    for _ in range(len(input)):
        counter += 1
        temp = input.pop()
        new = (temp * 3) % lcm_worry
        if new % 2 == 0:
            monkey1.append(new)
        else:
            monkey4.append(new)
    return counter

def m1(input):
    counter = 0
    for _ in range(len(input)):
        counter += 1
        temp = input.pop()
        new = (temp * 19) % lcm_worry
        if new % 7 == 0:
            monkey3.append(new)
        else:
            monkey5.append(new)
    return counter

def m2(input):
    counter = 0
    for _ in range(len(input)):
        counter += 1
        temp = input.pop()
        new =  (temp + 2) % lcm_worry
        if new % 11 == 0:
            monkey4.append(new)
        else:
            monkey0.append(new)
    return counter

def m3(input):
    counter = 0
    for _ in range(len(input)):
        counter += 1
        temp = input.pop()
        new = (temp * temp) % lcm_worry
        if new % 19 == 0:
            monkey7.append(new)
        else:
            monkey6.append(new)
    return counter
def m4(input):
    counter = 0
    for _ in range(len(input)):
        counter += 1
        temp = input.pop()
        new = (temp + 8) % lcm_worry
        if new % 3 == 0:
            monkey5.append(new)
        else:
            monkey1.append(new)
    return counter
def m5(input):
    counter = 0
    for _ in range(len(input)):
        counter += 1
        temp = input.pop()
        new = (temp + 6) % lcm_worry
        if new % 5 == 0:
            monkey3.append(new)
        else:
            monkey6.append(new)
    return counter
def m6(input):
    counter = 0
    for _ in range(len(input)):
        counter += 1
        temp = input.pop()
        new = (temp + 7) % lcm_worry
        if new % 17 == 0:
            monkey7.append(new)
        else:
            monkey2.append(new)
    return counter
def m7(input):
    counter = 0
    for _ in range(len(input)):
        counter += 1
        temp = input.pop()
        new = (temp + 4) % lcm_worry
        if new % 13 == 0:
            monkey2.append(new)
        else:
            monkey0.append(new)
    return counter

totals = [0] * 8
for _ in range(10000):
    totals[0]+= m0(monkey0)
    totals[1]+= m1(monkey1)
    totals[2]+= m2(monkey2)
    totals[3]+= m3(monkey3)
    totals[4]+= m4(monkey4)
    totals[5]+= m5(monkey5)
    totals[6]+= m6(monkey6)
    totals[7]+= m7(monkey7)
monkey_biz = sorted(totals)[-2:]
print(monkey_biz[0]*monkey_biz[1])





# monkey0 = [79,98]
# monkey1 = [54,65,75,74]
# monkey2 = [79,60,97]
# monkey3 = [74]
# worry_ops = [23,19,13,17]
# lcm_worry = lcm(*worry_ops)

# def m0(input):
#     counter = 0
#     for _ in range(len(input)):
#         counter += 1
#         temp = input.pop()
#         new = (temp * 19) % lcm_worry
#         if new % 23 == 0:
#             monkey2.append(new)
#         else:
#             monkey3.append(new)
#     return counter

# def m1(input):
#     counter = 0
#     for _ in range(len(input)):
#         counter += 1
#         temp = input.pop()
#         new = (temp + 6) % lcm_worry
#         if new % 19 == 0:
#             monkey2.append(new)
#         else:
#             monkey0.append(new)
#     return counter

# def m2(input):
#     counter = 0
#     for _ in range(len(input)):
#         counter += 1
#         temp = input.pop()
#         new =  (temp*temp) % lcm_worry
#         if new % 13 == 0:
#             monkey1.append(new)
#         else:
#             monkey3.append(new)
#     return counter

# def m3(input):
#     counter = 0
#     for _ in range(len(input)):
#         counter += 1
#         temp = input.pop()
#         new = (temp + 3) % lcm_worry
#         if new % 17 == 0:
#             monkey0.append(new)
#         else:
#             monkey1.append(new)
#     return counter

# totals = [0] * 4
# for _ in range(10000):
#     totals[0]+= m0(monkey0)
#     totals[1]+= m1(monkey1)
#     totals[2]+= m2(monkey2)
#     totals[3]+= m3(monkey3)

# print(sorted(totals)[-2:])