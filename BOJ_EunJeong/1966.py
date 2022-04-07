T = int(input())

for i in range(T):
    N = list(map(int, input().split()))
    Doc = list(map(int, input().split()))
    new = []

    for i in range(len(Doc)):
        Add = (Doc[i],i)
        new.append(Add)

    i = 0
    while True:
        if new[i][0] != max(Doc):
            new.append((new[i][0],new[i][1]))
            del new[i]
        else:
            Doc.remove(max(Doc))
            i+=1
        if i == N[0]:
            break

    for i in range(len(new)):
        if new[i][1] == N[1]:
            print(i+1)
