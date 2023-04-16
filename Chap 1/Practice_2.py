# 최대공약수 문제
# 두 자연수 a와 b의 최대 공약수(Greatest Common Divisor)를 구해봅시다.
# a와 b의 최대 공약수는 a의 약수인 동시에 b의 약수인 숫자 중에서 가장 큰 수를 의미합니다.
# 유클리드 알고리즘(Euclid’s algorithm)을 이용해 풀어봅시다.
# 1. a와 b에 저장될 자연수가 한 줄에 하나씩 주어집니다. 이때, a는 b보다 작지 않습니다. 값을 받아서 a와b에 각각 저장해 보세요.
# 2. 자연수 a와 b의 최대공약수를 return 하는 함수 gcd(a, b)를 완성해 보세요.

# 1번
a = int(input())
b = int(input())

# 2번
def gcd(a,b):
    while b!=0:
        r = a%b
        a=b
        b=r
    return a

# 출력
print("%d, %d의 최대공약수 = " %(a,b), gcd(a,b))