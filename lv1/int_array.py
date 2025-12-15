# https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    n = str(n)
    answer = list(n)
    answer.sort(reverse=True)
    answer = ''.join(answer)
    return int(answer)
