import sys
from collections import deque

input = sys.stdin.readline

def bfs(graph,start):
    num = [0]*(N+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a]+1
                visited.append(i)
                queue.append(i)
    return sum(num)


N,M = map(int,input().split())    # 유저의 수, 친구 관계의 수
relation = [[] for _ in range(N+1)] # 그래프 선언

for i in range(M):
    A,B = map(int,input().split())
    relation[A].append(B)
    relation[B].append(A)

result = []
for i in range(1,N+1):
    result.append(bfs(relation,i))

print(result.index(min(result))+1)
