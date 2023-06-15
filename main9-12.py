import random
# Task 9-12 game "Snake"

sizeA = 10
arr = []
x, y = 1, 1  # player  coordinates
x_temp, y_temp = 0, 0 # player temporary coordinates
x2, y2 = 0, 0  # enemies coordinates
enemy_num = 1
level = 1

# Fill data of matrix
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

print("\ngame \"Snake\"")
print("\nmatrix size {} x {}".format(sizeA, sizeA))

while True:

    arr[x][y] = '@'

    while True:
        x2 = random.randrange(1, 8)
        y2 = random.randrange(1, 8)
        if arr[x2][y2] == '@':
            continue
        else:
            arr[x2][y2] = '+'
            break

    move_num = 5
    print("Data:")
    print("\tGame level:\t", level)
    print("\tEnemy qty:\t", enemy_num)

    while True:

        # Print data of matrix
        for i in range(sizeA):
            if i == 0:
                print("\n\t", end='')
                for n in range(sizeA):
                    print(n + 1, end='  ')
                print()

            print(i + 1, end='\t')
            for j in range(sizeA):
                print(arr[i][j], end='  ')
            print()
        print("\nRemain move qty:\t", move_num)
        print("Player, move -> ")

        if move_num == 0:
            print("\tGAME OVER!")
            break

        x_temp = x
        y_temp = y

        y = abs(int(input("\t\tenter pos x: ")))
        x = abs(int(input("\t\tenter pos y: ")))

        if x > 10 or y > 10 or arr[x-1][y-1] == '*':
            move_num -= 1
            print("\n\tenter pos x.y correctly")
            continue
        else:
            move_num -= 1
            arr[x_temp][y_temp] = ' '
            x -= 1
            y -= 1
            if arr[x][y] != '+':
                arr[x][y] = '@'
                continue
            else:
                arr[x][y] = '@'
                break
