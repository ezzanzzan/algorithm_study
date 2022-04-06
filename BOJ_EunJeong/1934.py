T = int(input())

for i in range(T):
    num = 1
    A,B = map(int,input().split())
    for i in range(2,A+1):
        while A%i==0 and B%i==0:
            A = int(A/i)
            B = int(B/i)
            num = num*i
    print(num*A*B)
