import sys
input = sys.stdin.readline

n,m=map(int,input().split())
num,a,b = 2,1,1

while True:
    if n%num == 0 and m%num == 0:
        a = a * num
        b = b * num
        n = n // num
        m = m // num
    elif n < num or m < num:
        b = n * m * b
        break
    else:
        num+=1

print(a)
print(b)
