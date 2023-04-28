# 깊이 우선 탐색
# 완전 탐색적으로 그래프의 모든 정점을 방문하는 방법 중 깊이 우선 탐색(depth first search, DFS) 알고리즘을 구현해 봅시다.
# 1. 깊이 우선 탐색을 구현한 함수 dfs(graph, start, visit)를 완성해 보세요.
#   - 인자의 graph는 인접 리스트(딕셔너리와 집합)로 표현되어 있어요.
#   - start는 현재 정점이고, visited는 이미 방문한 집합이에요.
#   - 맨 처음에는 visited가 공집합으로 호출되어야 한다는 점에 유의하세요.
# 2. 인접 리스트(딕셔너리와 집합)로 이루어진 그래프 mygraph를 입력받아 보세요.

# 1번
def dfs(graph, start, visited):
    if start not in visited:
        visited.add(start)
        print(start, end=' ')
        nbr = graph[start] - visited
        for v in nbr:
            dfs(graph, v, visited)


# 2번
length = int(input())
mygraph = dict()
for i in range(length):
    e1,e2 = input().split()[:2]

    mygraph[e1] = mygraph.setdefault(e1, set()) | { e2 }
    mygraph[e2] = mygraph.setdefault(e2, set()) | { e1 }

# 출력
print('DFS : ', end='')
dfs(mygraph, "A", set())
print()