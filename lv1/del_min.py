# https://school.programmers.co.kr/learn/courses/30/lessons/12935v

# 제일 작은 수 제거하기- 중복을 못잡음

def solution(arr):
    arr.remove(min(arr))
    if arr == []:
        arr.append(-1)
    return arr


# 개선-시도중

def solution(arr):
    answer = []
    for i in arr:
        if i > min(arr):
            answer.append(i)
    if answer == []:
        answer.append(-1)
    return answer
