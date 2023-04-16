# 순차 탐색
# 탐색 대상인 리스트 A와 탐색 키 key를 입력받아 리스트의 모든 항목(A[0] ~ A[len(A)-1])을 순서대로 key와 비교하여 같으면 그 인덱스를 반환해 봅시다.
# 1. 탐색 대상인 리스트 A의 모든 항목을 순서대로 key와 비교하여 같으면 그 위치(인덱스)를 반환하고, 찾으려는 key 값이 리스트 A에 없으면 -1을 반환하는 순차 탐색 함수 sequential_search(A, key)를 완성해 보세요.
# 2. 리스트 A와 탐색 키 key를 입력받아 보세요.

# 1번
def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1

# 2번
A = [int(n) for n in input().split()]
key = int(input())

# 출력
print("%d찾기:" %(key), sequential_search(A, key))
