import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
de = deque()
for i in range(N):
    Command = input()
    if 'push_front' in Command:
        num = Command[11:]
        de.appendleft(int(num))
    elif 'push_back' in Command:
        num = Command[10:]
        de.append(int(num))
    elif 'pop_front' in Command:
        if not de:
            print("-1")
        else:
            print(de[0])
            de.popleft()
    elif 'pop_back' in Command:
        if not de:
            print("-1")
        else:
            print(de[-1])
            de.pop()
    elif 'size' in Command:
        print(len(de))
    elif 'empty' in Command:
        if not de:
            print("1")
        else:
            print("0")
    elif 'front' in Command:
        if not de:
            print("-1")
        else:
            print(de[0])
    elif 'back' in Command:
        if not de:
            print("-1")
        else:
            print(de[-1])
