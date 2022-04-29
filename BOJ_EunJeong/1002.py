import sys
import math

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    dis = abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2

    # 두 원이 같은 경우 : 위치의 개수가 무한대
    if x1 == x2 and y1 == y2 and r1 == r2:
        print("-1")
    # 두 원이 만나지 않는 경우
    elif dis > (r1+r2)**2 or dis < abs(r1-r2)**2:
        print("0")
    # 두 원이 외접, 내접 하는 경우
    elif dis == (r1+r2)**2 or dis == abs(r1-r2)**2:
        print("1")
    else:
        print("2")
