# 자연수의 제곱 계산 문제 - O(1), O(n), O(n²)
# 자연수 n이 주어졌을 때, n²을 구해봅시다. 복잡도가 O(1), O(n), O(n²) 이 되게 만들어 봅시다.
# 1. 각 compute_square_A(n), compute_square_B(n), compute_square_C(n) 함수로 다음과 같이 n의 제곱 값이 출력되는 함수를 작성해 보세요.
# 2. 변수 n에 자연수를 입력받아 저장해 보세요.

# 1번
def compute_square_A(n):
    return n*n

def compute_square_B(n):
    sum = 0
    for i in range(n):
        sum = sum + n
    return sum

def compute_square_C(n):
    sum = 0
    for i in range(n):
        for j in range(n):
            sum = sum + 1
    return sum

# 2번
n = int(input())

# 출력
print(compute_square_A(n))
print(compute_square_B(n))
print(compute_square_C(n))