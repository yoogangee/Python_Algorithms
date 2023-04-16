# 리스트의 중복 항목 탐색 문제
# n개의 항목으로 이루어진 어떤 리스트 A가 주어졌습니다. A에 중복된 항목이 있는지 없는지를 검사해 봅시다.
# 1. 공백으로 구분되어 입력되는 숫자들을 받아서 리스트 A에 저장해 보세요.
# 2. 같은 항목이 있으면 False를, 같은 항목이 없으면 True를 반환하는 함수 unique_elements(A)를 완성해 보세요.

# 1번
A = [int(n) for n in input().split()]

# 2번
def unique_elements(A):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            if A[i] == A[j]:
                return False
    return True

# 출력
print(unique_elements(A))