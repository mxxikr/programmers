"""
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

두 수는 1이상 1000000이하의 자연수입니다.
"""
def solution(n, m):
    answer = []

    # 최대 공약수
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break

    # 최소 공배수
    for i in range(max(n, m), n*m+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
    return answer

# 최대 공약수
## 두 수 이상의 여러 수의 공약수 중 최대인 수

# 최소 공배수
## 두 수 이상의 여러 수의 공배수 중 최소인 수