import sys

input = sys.stdin.readline

def move(N,start,to):
    print(start,to)

def hanoi(N,start,to,via):
    if N==1:
        move(N,start,to)
    else:
        hanoi(N-1,start,via,to)
        move(N,start,to)
        hanoi(N-1,via,to,start)

if __name__ == '__main__':
    N = int(input())
    start,via,to = 1,2,3

    print(2**N-1)
    total = hanoi(N,start,to,via)
