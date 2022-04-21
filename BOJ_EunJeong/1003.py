import sys
input = sys.stdin.readline

zero = [1,0]
one = [0,1]
T = int(input())

def fibonacci(n):
    lenght = len(zero)
    if n>=lenght:
        for i in range(lenght, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n],one[n])

for i in range(T):
    fibonacci(int(input()))
