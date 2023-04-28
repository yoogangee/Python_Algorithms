# 문자열 매칭 문제
# 길이가 n인 입력 문자열 T와 길이가 m인 패턴 문자열 P가 있습니다.
#   - 항상 n >= m이라고 가정합니다.
#   - 모든 문자열은 알파벳과 띄어쓰기만으로 구성되어 있다고 가정합니다.
#   - 대문자와 소문자를 구분합니다. 예를 들어, ‘a’와 ‘A’를 다른 문자로 취급합니다.
# T에서 가장 먼저 나타나는 P의 위치를 찾아봅시다. 패턴이 없으면 -1을 반환합니다.
# 1. T에서 가장 먼저 나타나는 P의 위치를 찾으면 그 인덱스를 반환하고, 패턴이 없으면 -1을 반환하는 함수 string_matching(T, P)을 완성해 보세요.
# 2. 입력 문자열 T와 패턴 문자열 P를 입력받아 보세요.

# 1번
def string_matching(T, P):
    n = len(T)
    m = len(P)
    for i in range(n-m+1):
        j = 0
        while j < m and P[j] == T[i+j]:
            j = j + 1
        if j == m:
            return i
    return -1

# 2번
T = input()
P = input()

# 출력
print(string_matching(T, P))