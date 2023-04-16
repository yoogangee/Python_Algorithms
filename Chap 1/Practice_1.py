# 최댓값을 찾는 알고리즘
# n개의 숫자가 들어있는 배열(또는 리스트) A에서 최댓값을 찾아봅시다.
# 1. 리스트 A의 모든요소들 중 최댓값을 찾아 return 하는 함수 find_max( A )를 완성해 보세요.
# 2. 공백으로 구분되어 입력되는 숫자들을 받아서 array에 저장해 보세요.

# 1번
def find_max(A):
    max = A[0]
    for i in range(len(A)):
        if A[i] > max:
            max = A[i]
    return max

# 2번
array = [int (n) for n in input().split()]

# 출력
print(array, "최댓값: ", find_max(array))