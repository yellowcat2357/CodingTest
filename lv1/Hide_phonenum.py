# https://school.programmers.co.kr/learn/courses/30/lessons/12948

# 핸드폰 번호 가리기- 문자열 곱셈 활용하면 더 쉽게 할 수 있었음

def solution(phone_number):
    answer = ''
    for i in phone_number[0:-4]:
        i = "*"
        answer += i
    for i in phone_number[-4:]:
        answer += i
    return answer
