from random import randint
board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]


def check_line(x, a, b, c):
    if board[a] == x and board[b] == x and board[c] == x:
        return True
    return False


def check_all(x):
    if check_line(x, 0, 1, 2):
        return True
    if check_line(x, 3, 4, 5):
        return True
    if check_line(x, 6, 7, 8):
        return True
    if check_line(x, 0, 4, 8):
        return True
    if check_line(x, 6, 4, 2):
        return True
    if check_line(x, 0, 3, 6):
        return True
    if check_line(x, 1, 4, 7):
        return True
    if check_line(x, 2, 5, 8):
        return True

    return False


def empty_box():
    for i in range(0, 9):
        if board[i] != 'x' and board[i] != 'o':
            return True


def printf(a, b, c):
    print(board[a], '|', board[b], '|', board[c], '|')
    print('-----------')


def show():
    printf(0, 1, 2)
    printf(3, 4, 5)
    printf(6, 7, 8)

show()

who_win = 0
while empty_box():
    box = input("Chọn vị trí (0-8): ")
    box = int(box)
    if board[box] == 'x' or board[box] == 'o':
        print('Ô đã có X hoặc O')
    else:
        board[box] = 'x'
        while empty_box():
            compute = randint(0, 8)
            if board[compute] == 'x' or board[compute] == 'o':
                pass
            else:
                board[compute] = 'o'
                break
    show()
    if check_all('x'):
        who_win = 'you'
        break

    if check_all('o'):
        win = 'computer'
        break

if who_win == 0:
    print('Hòa')
else:
    print(who_win, ' win')

