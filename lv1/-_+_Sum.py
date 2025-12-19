# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    nums = 0
    while nums < len(absolutes):
        if signs[nums]:
            answer += absolutes[nums]
            nums += 1
        else:
            answer -= absolutes[nums]
            nums += 1
    return answer
