# https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    if a < b:
        while a <= b:
            answer += a
            a += 1
    elif a > b:
        while b <= a:
            answer += b
            b += 1
    elif a == b:
        answer = a
    return answer
