import os

def generation_board(size):
    board = []
    for i in range(size):
        board.append(['.'] * size)
    return board


def print_board(board,size):
    char = 0
    i = 1
    h = []
    while (i <= size):
        h.append(str(i))
        i = i + 1
    x = ' '.join(h)
    print('        '+ x)
    print('        '+'v '*size)
    print('       '+'__'*size)
    for element in board:
        char += 1
        element = ' '.join(element)
        print(chr(char + 64).rjust(2), "=>", "|", element, "|")
    print('       '+'--'*size)
    return board

def player():
    a = True
    while a:
        row = input("Select a letter: ").upper()
        if row.isalpha():
            a = False
    b = True     
    while b:
        col = input("Select a number: ")
        if col.isnumeric():
            b = False
    return row, col

def set_of_coordinates(row_selected, col_selected):
    options_to_choose = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
     "1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9}
    row = options_to_choose[row_selected]
    col = options_to_choose[col_selected]
    return row, col

def select_coordinates():
    cell_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    row_selected,col_selected = player()
    if row_selected and col_selected in cell_list:
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
        row_selected, col_selected=select_position(board)
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
                    clear()
                    print("\nНou can't put a ship here! Try again\n")
                    print_board(board, size)
                    ask_for_single_ship(board, single_ship, i, size)
        else:
            clear()
            print("\nНou can't put a ship here! Try again\n")
            print_board(board, size)
            ask_for_single_ship(board, single_ship, i, size)

def ask_for_double_ship(board):
    z = 0
    print("Settle the waters with your two destroyers that take up two grids each !")
    while z != 2:
        print('''Whether the vessel is to be placed horizontally or vertically ?
   1 = Horizontally
   2 = Vertical ''')
        a = int(input("1 or 2: "))
        row_selected,col_selected = select_position(board)
        if a == 1:
            board[row_selected][col_selected] = "X"
            board[row_selected][col_selected+1] = "X"
            z +=1
            print_board(board, size)
        elif a == 2:
            board[col_selected][row_selected] = "X"
            board[col_selected+1][row_selected] = "X"
            z +=1
            print_board(board, size)           

def ask_for_triple_ship(board):  
    print_board(board, size)
    print("""Your aircraft carrier is waiting for you, show it to its launching point! 
    Remember that it occupies 3 grids on your map!""")
    print('''Whether the vessel is to be placed horizontally or vertically ?
   1 = Horizontally
   2 = Vertical ''')
    a = int(input("1 or 2: "))
    row_selected, col_selected=select_position(board)
    if a == 1:
        board[row_selected][col_selected] = "X"
        board[row_selected][col_selected+1] = "X"
        board[row_selected][col_selected+2] = "X"
        print_board(board, size)
    if a == 2:
        board[row_selected][col_selected] = "X"
        board[row_selected+1][col_selected] = "X"
        board[row_selected+2][col_selected] = "X"
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
        clear()        
    return board_player_1, board_player_2


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
            board_for_note_player_1[row1][col1] = 'H'
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
            board_for_note_player_2[row1][col1] = 'H'
            print_board(board_for_note_player_2, size)
            print("You've hit a ship!")
            player2 = True
            win(board_for_note_player_2)
    shooting_phase(player1, player2)


def win(board):
    list_of_hitting = []
    for row in board:
        for i in row:
            if i == "H":
                list_of_hitting.append(i)
    a = 0
    for i in range(len(list_of_hitting)):
        a = i
    if a == 9:
        print("\n\n\n  YOU WIN!\n\n\n")
        exit()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def size_of_the_board():
    print('    Select board size')
    size = int(input('Specify the map size from 5 to 10: '))
    if size >= 5 and size <=10:
        return size
    else:
        print('Wrong map size, please enter corect map size!')
        size_of_the_board()

def select_position(board):
    
    while True:
        row_selected, col_selected = select_coordinates()
        if board[row_selected][col_selected] != "X":
            return row_selected, col_selected
        else:
            clear()
            print("\nThis spot is occupied by batleship. Please spot again\n")
            print_board(board, size)


if __name__ == "__main__":
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