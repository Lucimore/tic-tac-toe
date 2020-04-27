# write your code here
#user_input = input("Enter cells: ")

flag = -1

#field = [[user_input[0], user_input[1], user_input[2]],
#         [user_input[3], user_input[4], user_input[5]],
#         [user_input[6], user_input[7], user_input[8]]]
field = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]


def print_board(field):
    print("---------")
    print('| {} {} {} |'.format(field[0][0], field[0][1], field[0][2]))
    print('| {} {} {} |'.format(field[1][0], field[1][1], field[1][2]))
    print('| {} {} {} |'.format(field[2][0], field[2][1], field[2][2]))
    print("---------")


def is_winner():
    for i in range(0, 3):
        if field[i][0] == field[i][1] == field[i][2]:  # rows
            if field[i][0] != ' ':
                return f'{field[i][0]} wins'
        elif field[0][i] == field[1][i] == field[2][i]:  # columns
            if field[0][i] != ' ':
                return f'{field[0][i]} wins'
        elif field[0][0] == field[1][1] == field[2][2]:  # left diagonal
            if field[0][0] != ' ':
                return f'{field[0][0]} wins'
        elif field[0][2] == field[1][1] == field[2][0]:  # right diagonal
            if field[0][2] != ' ':
                return f'{field[0][2]} wins'
    return 0


def is_finished_or_draw():
    counter = 0
    for i in field:
        for j in i:
            if j == ' ':
                counter += 1
    if counter == 0:
        return 'Draw'
    else:
        return -1


def is_possible():
    x_count = 0
    o_count = 0
    for i in field:
        for j in i:
            if j == 'X':
                x_count += 1
            if j == 'O':
                o_count += 1
    if abs(x_count - o_count) >= 2:
        return 'Impossible'
    winner_counter = 0
    for i in range(0, 3):
        if field[i][0] == field[i][1] == field[i][2]:  # rows
            if field[i][0] != ' ':
                winner_counter += 1
        elif field[0][i] == field[1][i] == field[2][i]:  # columns
            if field[0][i] != ' ':
                winner_counter += 1
    if winner_counter > 1:
        return 'Impossible'
    return 0



def check_input(coordinates):
    if len(coordinates) > 2:
        print('You should enter only two numbers!')
        return -1
    for x in coordinates:
        if not x.isdigit():
            print('You should enter numbers!')
            return -1
        if int(x) not in range(1, 4):
            print('Coordinates should be from 1 to 3!')
            return -1


def check_cell(coordinates):
    global flag
    x, y = 0, 0
    if coordinates == [1, 1]:
        x, y = 2, 0
    elif coordinates == [1, 2]:
        x, y = 1, 0
    elif coordinates == [1, 3]:
        x, y = 0, 0
    elif coordinates == [2, 1]:
        x, y = 2, 1
    elif coordinates == [2, 2]:
        x, y = 1, 1
    elif coordinates == [2, 3]:
        x, y = 0, 1
    elif coordinates == [3, 1]:
        x, y = 2, 2
    elif coordinates == [3, 2]:
        x, y = 1, 2
    elif coordinates == [3, 3]:
        x, y = 0, 2
    if field[x][y] != ' ':
        print("This cell is occupied! Choose another one!")
        return -1
    if flag == -1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'
    flag = -flag



def play():
    while True:
        coordinates = input("Enter the coordinates: ").split()
        if check_input(coordinates) == -1:
            continue
        coordinates = list(map(int, coordinates))
        if check_cell(coordinates) == -1:
            continue
        print_board(field)
        if is_possible() != 0:
            print(is_possible())
            break
        if is_winner() != 0:
            print(is_winner())
            break
        if is_finished_or_draw() == -1:
            continue
        else:
            print(is_finished_or_draw())
            break


print_board(field)
play()
