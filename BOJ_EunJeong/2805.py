import sys
input = sys.stdin.readline

N, M = map(int,input().split())
tree = list(map(int, input().split()))
start, end = 0, max(tree)

while start <= end:
    mid = (start + end)//2
    result = 0
    for i in tree:
        if i >= mid:
            result += i-mid
    if result >= M:
        start = mid + 1
    else:
        end = mid - 1

if end<mid:
    print(end)
else:
    print(mid)
