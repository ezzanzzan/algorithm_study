import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(N)
    while queue:
        x = queue.popleft()
        if x == K:
            print(dist[x])
            break
        for i in (x-1,x+1,x*2):
            if 0 <= i <= MAX and not dist[i]:
                dist[i] = dist[x]+1
                queue.append(i)

MAX = 100000
N,K = map(int,input().split())
dist = [0 for i in range(MAX+1)]

bfs()
