import sys
from collections import Counter

input = sys.stdin.readline

N, M, B = map(int,input().split())
land = Counter()
_time,_height,_sum,_block = 99999999,0,0,0
_top, _bottom = 0,256

for _ in range(N):
    line = list(map(int,input().split()))
    _block += sum(line)
    if _top < max(line): _top = max(line)
    if _bottom > min(line): _bottom = min(line)
    land.update(line)

for h in range(_bottom,_top+1):
    if (h*N*M) - _block > B:
        continue
    one,two = 0,0
    for i in land:
        if i < h:
            two += (h - i)*land[i]
        else:
            one += (i - h)*land[i]
    if _time >= (one*2+two):
        _time = one*2+two
        if _height < h:
            _height = h
print(_time,_height)
