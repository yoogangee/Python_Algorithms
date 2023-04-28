# 너비 우선 탐색
# 1. 너비 우선 탐색을 구현한 함수 bfs(graph, start)를 완성해 보세요.
#     - 인자의 graph는 인접 리스트(딕셔너리와 집합)로 표현되어 있어요.
#     - start는 시작 정점이에요.
#     - 너비 우선 탐색 알고리즘을 위해서는 자료구조 큐가 필요한데, 파이썬의 queue 모듈을 사용해 보세요.
# 2. 인접 리스트(딕셔너리와 집합)로 이루어진 그래프 mygraph를 입력받아 보세요.

import queue
# 1번을 해보세요!
def bfs(graph, start):
    visited = { start }
    que = queue.Queue()
    que.put(start)
    while not que.empty():
        v = que.get()
        print(v,end=' ')
        nbr = graph[v] - visited
        for u in nbr:
            visited.add(u)
            que.put(u)


# 2번을 해보세요!
mygraph = dict()
length = int(input())
for i in range(length):
    e1,e2 = input().split()[:2]

    mygraph[e1] = mygraph.setdefault(e1, set())|{e2}
    mygraph[e2] = mygraph.setdefault(e2, set())|{e1}

# 출력합니다!
print('BFS : ', end='')
bfs(mygraph, "A")
print()
