# https://school.programmers.co.kr/learn/courses/30/lessons/12919

# 서울에서 김서방 찾기- index 함수 사용시 더 짧게 가능


def solution(seoul):
    x = 0
    for i in seoul:
        if i == 'Kim':
            break
        else:
            x += 1
    return '김서방은 %d에 있다'%(x)
