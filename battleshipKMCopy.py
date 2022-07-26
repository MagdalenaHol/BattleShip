import os
import time
import graphic
import entrance


def generation_board(size):
    board = []
    for i in range(size):
        board.append(['.'] * size)
    return board


def print_board(board, size):
    char = 0
    i = 1
    h = []
    while (i <= size):
        h.append(str(i))
        i = i + 1
    x = ' '.join(h)
    print('        ' + x)
    print('        '+'v '*size)
    print('       '+'__'*size)
    for element in board:
        char += 1
        element = ' '.join(element)
        print(chr(char + 64).rjust(2), "=>", "|", element, "|")
    print('       '+'--'*size)
    return board


def player():
    while True:
        row = input("Select a letter: ").upper()
        if row.isalpha():
            break
    while True:
        col = input("Select a number: ")
        if col.isnumeric():
            break
    return row, col


def set_of_coordinates(row_selected, col_selected):
    options_to_choose = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
                         "1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9}
    row = options_to_choose[row_selected]
    col = options_to_choose[col_selected]
    return row, col


def select_coordinates():
    cell_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                 "J", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    row_selected, col_selected = player()
    if row_selected in cell_list and col_selected in cell_list:
        row, col = set_of_coordinates(row_selected, col_selected)
        return row, col
    else:
        print("Invalid input! You must select a cell on the board")
        select_coordinates()


# Poniżej widzimy pomnik ludzi światłych i wspaniałych, ludzi którzy pomimo mroku dziejów przebrneli przez bagno
# życia by dotrzeć do momentu w którym się znaleźli. Dzięki tym ludziom powstał ten oto fragemnt kodu !!!
def ask_for_single_ship(board, single_ship, i, size):
    if i <= 2:
        print("Deploy", single_ship, "single ships")
        row_selected, col_selected = select_position(board)
        if board[row_selected-1][col_selected] != "X":
            if row_selected + 1 == size:
                if board[row_selected][col_selected - 1] != "X":
                    if col_selected + 1 == size:
                        board[row_selected][col_selected] = "X"
                        clear()
                        print_board(board, size)
                        i += 1
                        single_ship -= 1
                        ask_for_single_ship(board, single_ship, i, size)
                    else:
                        if board[row_selected][col_selected + 1] != "X":
                            board[row_selected][col_selected] = "X"
                            clear()
                            print_board(board, size)
                            i += 1
                            single_ship -= 1
                            ask_for_single_ship(board, single_ship, i, size)
                        else:
                            clear()
                            print("\nНou can't put a ship here! Try again\n")
                            print_board(board, size)
                            ask_for_single_ship(board, single_ship, i, size)
                else:
                    clear()
                    print("\nНou can't put a ship here! Try again\n")
                    print_board(board, size)
                    ask_for_single_ship(board, single_ship, i, size)
            else:
                if board[row_selected + 1][col_selected] != "X":
                    if board[row_selected][col_selected - 1] != "X":
                        if col_selected + 1 == size:
                            board[row_selected][col_selected] = "X"
                            clear()
                            print_board(board, size)
                            i += 1
                            single_ship -= 1
                            ask_for_single_ship(board, single_ship, i, size)
                        else:
                            if board[row_selected][col_selected + 1] != "X":
                                board[row_selected][col_selected] = "X"
                                clear()
                                print_board(board, size)
                                i += 1
                                single_ship -= 1
                                ask_for_single_ship(
                                    board, single_ship, i, size)
                            else:
                                clear()
                                print("\nНou can't put a ship here! Try again\n")
                                print_board(board, size)
                                ask_for_single_ship(
                                    board, single_ship, i, size)
                    else:
                        clear()
                        print("\nНou can't put a ship here! Try again\n")
                        print_board(board, size)
                        ask_for_single_ship(board, single_ship, i, size)
                else:
                    clear()
                    print("\nНou can't put a ship here! Try again\n")
                    print_board(board, size)
                    ask_for_single_ship(board, single_ship, i, size)
        else:
            clear()
            print("\nНou can't put a ship here! Try again\n")
            print_board(board, size)
            ask_for_single_ship(board, single_ship, i, size)

def is_unoccupied(row, col, board):
    if (col < 0 or col > len(board[0])-1 or row < 0 or row > len(board)-1):
        return True
    else:
        return board[row][col] == "."


def ask_for_single_ship_clear(board):
    row_selected, col_selected = select_position(board)
    while True:
        if not (is_unoccupied(row_selected, col_selected, board) and
                is_unoccupied(row_selected + 1, col_selected, board) and \
                is_unoccupied(row_selected - 1, col_selected, board) and \
                is_unoccupied(row_selected, col_selected + 1, board) and \
                is_unoccupied(row_selected, col_selected-1, board)):
            break;

def validation():
    b = True
    while b:
        num = input("1 or 2: ")
        if num.isnumeric():
            if num > '2' or num < '1':
                print('Enter the correct value')
            else:
                b = False
    return num


def ask_for_double_ship(board):
    z = 0
    print("Settle the waters with your two destroyers that take up two grids each !")
    while z != 2:
        print('''Whether the vessel is to be placed horizontally or vertically ?
   1 = Horizontally
   2 = Vertical ''')
        direction_number = validation()
        row_selected, col_selected = select_position(board)
        if direction_number == '1':
            if col_selected < size - 1:
                board[row_selected][col_selected] = "X"
                board[row_selected][col_selected+1] = "X"
                z += 1
                print_board(board, size)
            else:
                print("Wrong ship's location, My Lord.")
                print_board(board, size)
        elif direction_number == '2':
            if row_selected < size - 1:
                board[row_selected][col_selected] = "X"
                board[row_selected+1][col_selected] = "X"
                z += 1
                print_board(board, size)
            else:
                print("Wrong ship's location, My Lord.")
                print_board(board, size)


def ask_for_triple_ship(board):
    print_board(board, size)
    print("""Your aircraft carrier is waiting for you, show it to its launching point! 
    Remember that it occupies 3 grids on your map!""")
    print('''Whether the vessel is to be placed horizontally or vertically ?
   1 = Horizontally
   2 = Vertical ''')
    while True:
        direction_number = validation()
        row_selected, col_selected = select_position(board)
        if direction_number == '1':
            if col_selected < size - 1 and col_selected < size - 2:
                board[row_selected][col_selected] = "X"
                board[row_selected][col_selected+1] = "X"
                board[row_selected][col_selected+2] = "X"
                print_board(board, size)
                break
            else:
                print("Wrong ship's location, My Lord.")
                print_board(board, size)

        if direction_number == '2':
            if row_selected < size - 1 and row_selected < size - 2:
                board[row_selected][col_selected] = "X"
                board[row_selected+1][col_selected] = "X"
                board[row_selected+2][col_selected] = "X"
                print_board(board, size)
                break
            else:
                print("Wrong ship's location, My Lord.")
                print_board(board, size)


def mark(board_player_1, board_player_2):
    print('''You have three kinds of ships.
    3 * X
    2 * XX
    1 * XXX
    Please mark the ships on the board\n''')
    player1 = True
    if player1 == True:
        print("Player 1")
        print_board(board_player_1, size)
        ask_for_single_ship(board_player_1, single_ship, i, size)
        ask_for_double_ship(board_player_1)
        ask_for_triple_ship(board_player_1)
        print("Player 1")
        time.sleep(5)
        clear()
        player1 = False
        player2 = True

    if player2 == True:
        print("Player 2")
        print_board(board_player_2, size)
        ask_for_single_ship(board_player_2, single_ship, i, size)
        ask_for_double_ship(board_player_2)
        ask_for_triple_ship(board_player_2)
        print("Player 2")
        time.sleep(5)
        clear()
    return board_player_1, board_player_2

def check_vertical_neirbous(from_field, to_field, step_size, col, opponent_board, board_for_note, row, set_as_sunk ):
    for x in range(from_field, to_field, step_size):
        if not is_unoccupied(x, col, opponent_board):
            if opponent_board[ x ][ col ] == "X" and board_for_note[x][col] != "H":
                board_for_note[ row ][ col ] = "H"
                return
            if board_for_note[ x ][ col ] == "H":
                set_as_sunk.append((x, col))
        else:
            break

def mark_as_hit_or_sunk(row, col, board_for_note, opponent_board):
    set_as_sunk = [(row,col)]
    check_vertical_neirbous(row+1,row+3, 1,  col, opponent_board, board_for_note, row, set_as_sunk)
    check_vertical_neirbous(row-1,row-3, -1,  col, opponent_board, board_for_note, row, set_as_sunk)
    for row, col in set_as_sunk:
        board_for_note[row][col] = "S"

def shooting_phase(player1, player2):
    print("try to shoot")
    if player1 == True:
        print("Player1")
        print_board(board_for_note_player_1, size)
        row1, col1 = select_coordinates()

        if board_player_2[row1][col1] == '.':
            board_for_note_player_1[row1][col1] = 'M'
            print("You've missed!")
            print_board(board_for_note_player_1, size)
            player1 = False
            player2 = True
        elif board_player_2[row1][col1] == 'X':
            mark_as_hit_or_sunk(row1, col1, board_for_note_player_1, board_player_2 )
            print_board(board_for_note_player_1, size)
            print("You've hit a ship!")
            player1 = True
            win(board_for_note_player_1)



    elif player2 == True:
        print("Player2")
        print_board(board_for_note_player_2, size)
        row1, col1 = select_coordinates()

        if board_player_1[row1][col1] == '.':
            board_for_note_player_2[row1][col1] = 'M'
            print("You've missed!")
            print_board(board_for_note_player_2, size)
            player1 = True
            player2 = False
        elif board_player_1[row1][col1] == 'X':
            mark_as_hit_or_sunk(row1, col1, board_for_note_player_1, board_player_2 )
            print_board(board_for_note_player_2, size)
            print("You've hit a ship!")
            player2 = True
            win(board_for_note_player_2)
    shooting_phase(player1, player2)


def win(board):
    sum = 0
    for row in board:
        for i in row:
            if i == "H":
                sum = sum + 1
    if sum == 10:
        print("\n\n\n  YOU WIN!\n\n\n")
        exit()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def size_of_the_board():
    import vhod
    print('    Select board size')
    while True:
        num = input("Specify the map size from 5 to 10: ")
        if num.isnumeric():
            if int(num) >= 5 and int(num) <= 100:
                a = num
                return int(a)
            else:
                print('Enter the correct value!')


def select_position(board):

    while True:
        row_selected, col_selected = select_coordinates()
        if board[row_selected][col_selected] != "X":
            return row_selected, col_selected
        else:
            clear()
            print("\nThis spot is occupied by batleship. Please spot again\n")
            print_board(board, size)


def graphic_ship():
    graphic.ship
    time.sleep(3)
    clear()


if __name__ == "__main__":
    graphic_ship()
    player1 = True
    player2 = False
    i = 0
    single_ship = 3
    size = size_of_the_board()
    board_player_1 = generation_board(size)
    board_player_2 = generation_board(size)
    board_for_note_player_1 = generation_board(size)
    board_for_note_player_2 = generation_board(size)
    mark(board_player_1, board_player_2)
    shooting_phase(player1, player2)
    # clear()
    # print("Spot your batleship")
    # clear()


# if input == "vertical":
#     if board[row][col] = "X":
#         if board[row][col] = "H":    # dla single
#             board[row][col] = "S"
#         if board[row][col] = "H" and board[row][col+1] = "H":   #dla double
#             board[row][col] = "S"
#             board[row+1][col] = "S"
#         if board[row][col] = "H" and board[row][col+1] = "H" and board[row][col+2] = "H":    #dla triple
#             board[row][col] = "S"
#             board[row][col+1] = "S"
#             board[row][col+2] = "S"
# elif input == "horisontal":
#     if board[row][col] = "H":   # dla single
#         board[row][col] = "S"
#     elif board[row][col] = "H" and board[row+1][col] = "H":   #dla double
#         board[row][col] = "S"
#         board[row+1][col] = "S"
#     elif board[row][col] = "H" and board[row+1][col] = "H" and board[row+2][col] = "H":    #dla triple
#         board[row][col] = "S"
#         board[row+1][col] = "S"
#         board[row+2][col] = "S"
