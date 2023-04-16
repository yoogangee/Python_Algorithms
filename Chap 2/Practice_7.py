# 자연수의 이진수 변환에서 총 비트 수 계산 - 순환
# 자연수 n을 이진수로 표시하였을 때 총 비트 수를 구해봅시다. 이때, 순환 구조로 총 비트 수를 구하는 알고리즘을 작성해 봅시다.
# 1. 자연수 n을 이진수로 표시하였을 때 총 비트 수를 return 하는 함수 binary_digits(n)를 완성해 보세요. 이때, 순환 구조로 알고리즘을 작성해 보세요.
# 2. 입력되는 양의 정숫값을 받아서 n에 저장해 보세요.

# 1번
def binary_digits(n):
    if n <= 1:
        return 1
    else:
        return 1+binary_digits(n//2)
# 2번
n = int(input())

# 출력
print(binary_digits(n))