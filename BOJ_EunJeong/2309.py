data = []

for i in range(9):
    data.append(int(input()))

data.sort()

for i in range(8):
    for j in range(i+1,9):
        num = sum(data) - data[i] - data[j]
        if num == 100:
            del data[i]
            del data[j-1]
            break
    if num == 100:
        break;

for i in data:
    print(i)
