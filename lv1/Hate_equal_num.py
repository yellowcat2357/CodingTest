# https://school.programmers.co.kr/learn/courses/30/lessons/12906

# 같은 숫자는 싫어-가장 최근에 리스트에 넣은걸 새로 넣을 항목과 비교하게 만들면 더 빠르게 할 수 있었음

def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer
