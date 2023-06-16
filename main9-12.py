import random
# Task 9-12 game "Snake"

sizeA = 10
arr = []
x_player, y_player = 1, 1  # player  coordinates
x_temp, y_temp = 0, 0  # player temporary coordinates
x2, y2 = 0, 0  # enemies coordinates
enemy_num, move_num, count, level = 0, 0, 0, 0
ind_move_y, ind_move_n, ind_enemy_done = 0, 0, 0  # counter of moves correct & not correct, enemy done
level_lim = 5
logic = False

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

arr[x_player][y_player] = '@'  # start position of player

print("\ngame \"Snake\"")
print("\nmatrix size {} x {}".format(sizeA, sizeA))

while level < level_lim:

    arr_enemy = []
    ind_arr_enemy = 0
    logic2 = True

    if logic:
        print("\tGAME OVER!")
        break

    # Refill data of matrix
    for i in range(sizeA):
        for j in range(sizeA):
            if arr[i][j] != '@' and arr[i][j] != '*':
                arr[i][j] = " "

    level += 1
    enemy_num += 1
    count += enemy_num
    for i in range(enemy_num):  # logic to fill data by random enemy "+"
        while True:
            arr_temp = []
            y2 = random.randrange(1, 8)
            arr_temp.append(y2)
            x2 = random.randrange(1, 8)
            arr_temp.append(x2)
            if arr[y2][x2] == '@' or arr[y2][x2] == '+':
                continue
            elif y2 == y_player or x2 == x_player:
                continue
            else:
                for k in range(ind_arr_enemy):
                    if y2 == arr_enemy[k][0] or x2 == arr_enemy[k][1]:
                        logic2 = False
                        break
            if logic2:
                arr[x2][y2] = '+'
                arr_enemy.append(arr_temp)
                ind_arr_enemy += 1
                break
            else:
                logic2 = True
                continue

    move_num += 5
    print("Data:")
    print("\tGame level:\t", level)
    print("\tEnemy qty:\t", enemy_num)

    while count != 0:

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

        if move_num == 0:
            logic = True
            break

        print("Player, move in orthogonal -> ")

        x_temp = x_player
        y_temp = y_player

        y = abs(int(input("\t\tenter pos x: ")))
        x = abs(int(input("\t\tenter pos y: ")))
        x -= 1
        y -= 1

        if x > 9 or y > 9 or arr[x][y] == '*' or arr[x][y] == 'o':
            print("\n\tenter pos x.y correctly")
            move_num -= 1
            ind_move_n += 1
            continue
        elif x == x_temp or y == y_temp:
            x_player = x
            y_player = y

            move_num -= 1
            arr[x_temp][y_temp] = 'o'

            for i2 in range(x_temp, x, (1 if x_temp < x else -1)):
                arr[i2][y] = 'o'
            for j2 in range(y_temp, y, (1 if y_temp < y else -1)):
                arr[x][j2] = 'o'

            if arr[x][y] != '+':
                arr[x][y] = '@'
                ind_move_y += 1
                continue
            else:
                arr[x][y] = '@'
                ind_enemy_done += 1
                ind_move_y += 1
                count -= 1
        else:
            print("\n\tenter pos x.y correctly")
            move_num -= 1
            ind_move_n += 1
            continue
else:
    # Refill data of matrix
    for i in range(sizeA):
        for j in range(sizeA):
            if arr[i][j] != '@' and arr[i][j] != '*':
                arr[i][j] = " "

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

    print("\n\tYOU WIN! END of GAME")
    print("\n\tData of report:")
    print("\t\tmove qty:")
    print("\t\t\tcorrect\t= ", ind_move_y)
    print("\t\t\tuncorrect\t= ", ind_move_n)
    print("\t\trate of winnings = ", ind_enemy_done)
