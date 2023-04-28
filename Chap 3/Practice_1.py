# 정렬 문제
# 리스트에 n개의 항목이 들어 있습니다. 이들을 키(key)의 순서에 따라 오름차순(non-decreasing order)으로 재배치해봅시다.
# 1. 제자리 정렬로 개선된 선택 정렬 알고리즘을 구현한 함수 selection_sort(A)를 완성해 보세요.
#     - 내부 루프의 최소 항목을 찾는 범위와 리스트의 두 항목을 서로 교환하는 코드에 유의하며 작성해 보세요.
#     - selection_sort(A) 함수 내에서 중간과정을 출력하는 함수 printStep(arr, val)을 호출해 선택 정렬의 전체 과정을 출력해 보세요.
# 2. 공백으로 구분되어 입력되는 숫자들을 받아서 리스트 A에 저장해 보세요.

# 1번
def selection_sort(A):
    for i in range(len(A)-1): # 맨 마지막 전까지만 하면됨
        min_idx = i
        for j in range(i+1,len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]
        printStep(A,i+1)
    return A

def printStep(arr, val):
    print("  Step %2d = " %val, end='')
    print(arr)

# 2번
A = [int(n) for n in input().split()]

# 출력
print("Original  :", A)
selection_sort(A)
print("Selection :", A)