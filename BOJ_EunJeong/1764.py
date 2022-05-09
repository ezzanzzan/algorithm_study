import sys
input = sys.stdin.readline

N,M = map(int,input().split())
nlist = dict()
nmlist = dict()
num = 0

for _ in range(N):
    s = input().strip()
    nlist[s] = 1
for _ in range(M):
    s = input().strip()
    if s in nlist:
        nmlist[s] = 1
        num += 1
print(num)
nmlist = sorted(nmlist.keys())
for i in nmlist:
    print(i)
