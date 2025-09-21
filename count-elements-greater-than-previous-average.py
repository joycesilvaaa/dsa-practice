#!/bin/python3

import math
import os
import random
import re
import sys



def average(numbers):
    return sum(numbers)/ len(numbers) if numbers else 0

def countResponseTimeRegressions(responseTimes):
    if not responseTimes:
        return 0
        
    days_numbers = len(responseTimes)
    if days_numbers == 1:
        return 0
    
    count = 0
    for number in range(1, days_numbers):
        previous_average = average(responseTimes[:number])
        if responseTimes[number] > previous_average:
            count += 1
    return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
