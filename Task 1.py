board = ['', '', '',
         '', '', ''
                 '', '', '']


def draw_board(board):
    print(' -------------------')
    for i in range(3):
        print(' | ', ' ', ' | ', ' ', ' | ', ' ', ' | ', ' ')
    print(' -------------------')


draw_board(board)

player = 'X' or 0


def ask_move(player, board):
    x, y = input(f"{player}, Введите х и у координаты (example: 0 0): ").strip().split()
    x, y = int(x), int(y)

    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        return (x, y)
    else:
        print("Клетка занята. Введите координаты еще раз.")
    return ask_move(player, board)


def make_move(player, board, x, y):
    if board[x][y] != " ":
        print("Клетка занята")
        return False
    else:
        board[x][y] = player
    return True


def ask_and_make_move(player, board):
    x, y = ask_move(player, board)


make_move(0, board, 2, 0)
