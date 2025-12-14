# https://school.programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    a = list()
    k = 1
    c = x
    while k <= n:
        c = x*k
        a.append(c)
        k += 1
    return a
