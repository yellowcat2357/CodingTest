# https://school.programmers.co.kr/learn/courses/30/lessons/12943

# 콜라츠 추측
            
def solution(num):
    trynum = 0
    while trynum < 500:
        if num == 1:
            break            
        elif num % 2 == 0:
            num = num/2
            trynum += 1
        else:
            num = num*3 + 1
            trynum += 1
    if trynum == 500:
        trynum = -1
    return trynum
