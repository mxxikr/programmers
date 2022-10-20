"""
자연수 n이 매개변수로 주어집니다. 
n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

n은 1 이상 100,000,000 이하인 자연수입니다.

n (10진법) = 45
n (3진법) = 1200
앞뒤 반전(3진법) = 0021
10진법으로 표현 = 7

n (10진법) = 125
n (3진법) = 11122
앞뒤 반전(3진법) = 22111
10진법으로 표현 = 229
"""
def solution(n):
    tmp = ''
    answer = 0
    while n >= 3:
        if n // 3 != 0:
            tmp += str(n % 3)
            n = n // 3
    tmp += str(n) # 3진법 변환한 수를 뒤집은 수
    
    # 10진법 변환
    for i in range(1, len(tmp)+1):
        answer += int(tmp[i-1]) * int(3**(len(tmp)-i))
    
    return answer