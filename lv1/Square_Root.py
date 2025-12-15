# https://school.programmers.co.kr/learn/courses/30/lessons/12934

import math

def solution(n):
    nums = list()
    sqrt = math.sqrt(n)
    if int(sqrt) == sqrt:
        return (sqrt + 1) ** 2
    return -1
