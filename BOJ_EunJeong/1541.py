import sys
input = sys.stdin.readline

_input = input()
_result = []
if '-' in _input:
    _input = _input.split('-')
    for i,x in enumerate(_input):
        if '+' in x:
            _result.append(sum(list(map(int,x.split('+')))))
        else:
            _result.append(int(x))
    result = _result[0]
    for i in range(1,len(_result)):
        result -= _result[i]
    print(result)
else:
    _result = _input.split('+')
    print(sum(list(map(int,_result))))
