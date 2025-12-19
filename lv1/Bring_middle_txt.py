# https://school.programmers.co.kr/learn/courses/30/lessons/12903

# 가운데 글자 가져오기-//연산자 사용하면 더 짧아짐

def solution(s):    
    if len(s) % 2 != 0:
        return s[int(len(s)/2)]
    return s[int(len(s)/2)-1] + s[int(len(s)/2)]
