import sys

input = sys.stdin.readline

memo = [[[0 for col in range(21)] for row in range(21)] for depth in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j == 0 or k == 0:
                memo[i][j][k] = 1

def w(a,b,c):
    if memo[a][b][c] != 0:
        return memo[a][b][c]
    else:
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        elif a < b and b < c:
            memo[a][b][c] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        else:
            memo[a][b][c] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
        return memo[a][b][c]

while True:
    a,b,c = map(int,input().split())

    if a == -1 and b == -1 and c == -1:
        break
    elif a <= 0 or b <= 0 or c <= 0:
        result = 1
    elif a > 20 or b > 20 or c > 20:
        result = w(20,20,20)
    else:
        result = w(a, b, c)
    print("w({}, {}, {}) = {}".format(a, b, c, result))
