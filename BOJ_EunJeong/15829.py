import sys
input = sys.stdin.readline

L = int(input())
S = input()
M = 1234567891
r = 31
result = 0

for i in range(L):
    result += (ord(S[i])-96) * (r**i)

print(result%M)
