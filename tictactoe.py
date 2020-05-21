field = [list(' ' * 3) for i in range(0, 9, 3)]
user_coordinate = {(1, 3): (0, 0), (2, 3): (0, 1), (3, 3): (0, 2),
                   (1, 2): (1, 0), (2, 2): (1, 1), (3, 2): (1, 2),
                   (1, 1): (2, 0), (2, 1): (2, 1), (3, 1): (2, 2)}
turn = 'X'


def game_field():
    print('-' * 9)
    for j in field:
        print(f'| {j[0]} {j[1]} {j[2]} |')
    print('-' * 9)


def fill_cell():
    global turn
    user_point = input('Enter the coordinates: ').split()
    if not user_point[0].isdigit() or not user_point[1].isdigit():
        print('You should enter numbers!')
    elif int(user_point[0]) not in range(1, 4) or int(user_point[1]) not in range(1, 4):
        print('Coordinates should be from 1 to 3!')
    else:
        real_point = user_coordinate[int(user_point[0]), int(user_point[1])]
        if field[real_point[0]][real_point[1]] != ' ':
            print('This cell is occupied! Choose another one!')
        else:
            if turn == 'X':
                field[real_point[0]][real_point[1]] = 'X'
                turn = 'O'
                game_field()
            elif turn == 'O':
                field[real_point[0]][real_point[1]] = 'O'
                turn = 'X'
                game_field()


def row():
    for i in field:
        if i[0] == i[1] == i[2]:
            return i[0]


def col():
    col_lst = []
    for item in range(len(field)):
        for column in range(len(field)):
            col_lst.append(field[column][item])
        if col_lst[0] == col_lst[1] == col_lst[2]:
            return col_lst[0]
        col_lst.clear()
 

def diagonal():
    d = []
    for i in range(len(field)):
        for j in range(len(field)):
            if i == j:
                d.append(field[i][j])
    if d[0] == d[1] == d[2]:
        return d[0]
    d.clear()
    for i in range(len(field)):
        for j in range(len(field) - 1, -1, -1):
            if i == abs(j - 2):
                d.append(field[i][j])
    if d[0] == d[1] == d[2]:
        return d[0]
    d.clear()


def x_wins():
    if diagonal() == 'X' or col() == 'X' or row() == 'X':
        return True


def o_wins():
    if diagonal() == 'O' or col() == 'O' or row() == 'O':
        return True


def draw():
    flag = 0
    for i in field:
        if ' ' not in i:
            flag += 1
    if flag == 3:
        return True


game_field()

while True:
    if x_wins():
        print('X wins')
        break
    elif o_wins():
        print('O wins')
        break
    elif draw():
        print('Draw')
        break
    fill_cell()
