N = int(input())
s = 666
while 1:
    if '666' in str(s):
        N -= 1
        if N == 0:
            break
    s = s + 1
print(s)
