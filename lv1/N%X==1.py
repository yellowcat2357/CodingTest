# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    x = 1
    while x < n:
        if n % x == 1:
            answer = x
            break
        elif n % x != 1:
            x += 1
            continue
    return answer
