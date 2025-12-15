# https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=python3

def solution(x):
    answer = 0
    for i in list(str(x)):
        answer += int(i)
    if x % answer == 0:
        answer = True
    else:    
        answer = False
    return answer
