import sys
input = sys.stdin.readline

N,r,c = map(int,input().split())
result = 0

while N >= 1:
    lenght = 2**(N-1)

    if r<lenght:
        if c<lenght:    # 1사분면
            if r == 0:
                if c == 1:
                    result += 1
                    break
            elif r == 1:
                if c == 0:
                    result += 2
                    break
                elif c == 1:
                    result += 3
                    break
        else:           # 2사분면
            result += lenght*lenght
            c = c - lenght
    else:
        if c<lenght:    # 3사분면
            result += lenght*lenght*2
            r = r - lenght
        else:           # 4사분면
            result += lenght*lenght*3
            r = r - lenght
            c = c - lenght
    N = N - 1

print(result)
