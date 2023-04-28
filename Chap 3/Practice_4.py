# 최근접 쌍의 거리 문제
# 2차원 평면상에 n개의 점이 있습니다. 가장 인접한 쌍의 거리를 구해봅시다.
#   - 두 점 사이의 거리를 계산할 때는 유클리드 거리(Euclidean distance)를 이용합니다.
#   - 유클리드 거리를 구할 때 math 모듈의 sqrt()와 거듭제곱 연산자를 사용해 봅시다.
# 1. 가능한 모든 점의 쌍에 대해 거리를 계산하고 가장 짧은 것을 찾는 함수 closest_pair(p)를 완성해 보세요. 코드가 너무 길어진다면 추가적인 함수를 정의하여 closest_pair(p) 내에서 호출해도 좋아요.
# 2. 점의 리스트 p를 입력받아 보세요. p는 [(x1, y1), …, (xn, yn)] 의 형태로 되어 있어요

# 1번
def distance(p1,p2):
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def closest_pair(p):
    min_dist = float('Inf')
    for i in range(len(p)-1):
        for j in range(1, len(p)-i):
            if min_dist > distance(p[i], p[i+j]):
                min_dist = distance(p[i], p[i+j])
    return min_dist


# 2번
length = int(input())
p = [tuple(int(m) for m in input().split()) for i in range(length)]

# 출력
print("최근접 거리:", closest_pair(p))
