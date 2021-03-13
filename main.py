#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(a):
    print(a)
    result = []
    sum_a = sum(a)
    seat_sum = 0
    sum_list = set()
    sum_tmp = 0
    seat_min = 0
    bus_seat = 0

    for item in a:
        seat_min = max(seat_min, item)
        sum_tmp += item
        sum_list.add(sum_tmp)

    for item in sum_list:
        
        if(item < seat_min):
            continue
        if(sum_a%item != 0):
            continue
        bus_seat = item

        seat_tmp = 0
        seat_sum = 0
        
        for row, col in enumerate(a):
            seat_tmp += col
            if(seat_tmp > bus_seat):
                break
            if(seat_tmp == bus_seat):
                seat_sum += col
                seat_tmp = 0
                if(seat_sum == sum_a):
                    result.append(bus_seat)
                    break
                continue
            if(seat_sum == sum_a):
                result.append(bus_seat)
                break
            seat_sum += col
            
    result.sort()
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
