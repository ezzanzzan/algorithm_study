N = input()
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort(reverse=True)

mul = [x*y for x,y in zip(A,B)]
print(sum(mul))
