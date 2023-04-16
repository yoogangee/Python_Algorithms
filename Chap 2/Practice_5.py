# 팩토리얼 알고리즘 - 반복
# 자연수 n의 팩토리얼을 계산해봅시다. 이때, 반복 구조의 팩토리얼 알고리즘을 구현해 봅시다.
# 1. 순환적인 팩토리얼 알고리즘을 반복 구조로 변환한 팩토리얼 함수 factorial(n)을 완성해 보세요.
# 2. 입력되는 자연수를 받아서 n에 저장해 보세요.

# 1번
def factorial(n):
    answer = 1
    for i in range(n):
        answer = answer*(n-i)
    return answer

# 2번
n = int(input())

# 출력
print(factorial(n))