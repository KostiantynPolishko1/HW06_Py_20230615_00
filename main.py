# Task 8 Вывести матрицу 10 на 10 заполненую символом * по границам

sizeA = 10
arr = []

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
                temp.append("-")
    arr.append(temp)

print("\nmatrix size {} x {}".format(sizeA, sizeA))
for i in arr:
    for j in i:
        print(j, end='  ')
    print()
