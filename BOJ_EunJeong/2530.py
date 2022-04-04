A,B,C = map(int,input().split())
D = int(input())

C = C + D

if C >= 60:
    B = B + int(C/60)
    C = C % 60
    if B >=60:
        A = A + int(B/60)
        B = B%60
        if A>=24:
            A = A % 24

print(A,B,C)
