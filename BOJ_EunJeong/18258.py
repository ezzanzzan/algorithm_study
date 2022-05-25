import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
queue = deque()

for i in range(N):
    arr = input()
    if 'push' in arr:
        queue.append(int(arr[4:]))
    elif 'pop' in arr:
        if not queue:
            print("-1")
        else:
            print(queue.popleft())
    elif 'size' in arr:
        print(len(queue))
    elif 'empty' in arr:
        if not queue:
            print("1")
        else:
            print("0")
    elif 'front' in arr:
        if not queue:
            print("-1")
        else:
            print(queue[0])
    elif 'back' in arr:
        if not queue:
            print("-1")
        else:
            print(queue[len(queue)-1])
