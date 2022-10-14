"""
두 정수 left와 right가 매개변수로 주어집니다. 
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

1 ≤ left ≤ right ≤ 1,000

다음 표는 13부터 17까지의 수들의 약수를 모두 나타낸 것입니다.
따라서, 13 + 14 + 15 - 16 + 17 = 43을 return 해야 합니다.

다음 표는 24부터 27까지의 수들의 약수를 모두 나타낸 것입니다.
따라서, 24 - 25 + 26 + 27 = 52를 return 해야 합니다.
"""

def solution(left, right):
    answer = 0

    for n in range(left, right+1):
        tmp = []
        
        for i in range(1, int(n**(1/2)) + 1):
            if (n % i == 0):
                tmp.append(i) 
                if ( (i**2) != n) : 
                    tmp.append(n // i)
            
        if len(tmp) % 2 == 0:
            answer += n
        else:
            answer -= n

    return answer