# 정렬되지 않은 리스트의 탐색 문제
# 리스트에 n개의 항목이 들어 있습니다. 이 리스트에서 “탐색키” 를 가진 항목을 찾아봅시다.
# 만약 찾는 항목이 있으면 그 항목의 인덱스를 반환하고, 없으면 -1을 반환해봅시다. 단, 리스트의 항목들은 정렬되어 있지 않습니다.
# 1. 순차 탐색을 구현하고 있으며 탐색키가 리스트에 있으면 그 항목의 인덱스를 반환하고, 없으면 -1을 반환하는 함수 sequential_search(A, key)를 완성해 보세요.
# 2. 공백으로 구분되어 입력되는 숫자들을 받아서 리스트 A에 저장해 보세요.
# 3. 탐색 키를 받아서 key에 저장해 보세요.

# 1번
def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1

# 2번
A = [int(n) for n in input().split()]

# 3번
key = int(input())

# 출력
print(sequential_search(A, key))