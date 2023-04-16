# 팩토리얼 알고리즘 - 순환
# 자연수 n의 팩토리얼을 계산해봅시다. 이때, 순환 관계식을 이용하여 순환적인 팩토리얼 알고리즘을 구현해 봅시다.
# 1. 팩토리얼의 순환 관계식(recurrence relation)의 정의에 따라 n! 을 구하는 순환적인 팩토리얼 함수 factorial(n)을 완성해 보세요.
# 2. 입력되는 자연수를 받아서 n에 저장해 보세요.

# 1번
n = int(input())

# 2번
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

# 출력
print(factorial(n))