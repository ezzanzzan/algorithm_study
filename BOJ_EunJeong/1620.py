import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Book = dict()
Book_ = []

for i in range(1,N+1):
    s = input().strip()
    Book[s] = i
    Book_.append(s)

for _ in range(M):
    s = input().strip()
    if s.isdigit():
        print(Book_[int(s)-1])
    else:
        print(Book[s])
