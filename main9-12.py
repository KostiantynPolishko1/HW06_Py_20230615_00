import random
# Task 9-12 game "Snake"

sizeA = 10
arr = []
x, y = 0, 0

for i in range(sizeA):
    temp = []
    if i == 0 or i == sizeA - 1:
        for j in range(sizeA):
            temp.append("*")
    else:
        for j in range(sizeA):
            if j == 0 or j == sizeA - 1:
                temp.append("*")
            else:
                temp.append(" ")
    arr.append(temp)

arr[1][1] = '@'

while True:
    x = random.randrange(1, 8)
    y = random.randrange(1, 8)
    if arr[x][y] == '@':
        continue
    else:
        arr[x][y] = '+'
        break

print("\nmatrix size {} x {}".format(sizeA, sizeA))

for i in range(sizeA):
    if i == 0:
        print("\n\t", end='')
        for n in range(sizeA):
            print(n + 1, end='  ')
        print()

    print(i+1, end='\t')
    for j in range(sizeA):
        print(arr[i][j], end='  ')
    print()
