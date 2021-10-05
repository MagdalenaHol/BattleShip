import os
import random

# Generation board
def generation_board(height, width):
    board = []
    for i in range(height):
        board.append(['.'] * width)
    return board

# Print board 5x5 
def print_board5_5(board):
    char = 0
    print('        1 2 3 4 5 ')
    print('        v v v v v ')
    print('       ___________')
    for element in board:
        char += 1
        element = ' '.join(element)
        print(chr(char + 64).rjust(2), "=>", "|", element, "|")
    print('       -----------')
    return board

# Print board 10x10
def print_board10_10(board):
    char = 0
    print('        1 2 3 4 5 6 7 8 9 10')
    print('        v v v v v v v v v v')
    print('       ____________________')
    for element in board:
        char += 1
        element = ' '.join(element)
        print(chr(char + 64).rjust(2), "=>", "|", element, "|")
    print('       --------------------')

coordinates_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}

# logic ai Player
def ai_player(coordinates):
    bot_move = random.choice(coordinates)
    coordinates.remove(bot_move)
    row = int(coordinates_dict[bot_move[0]])
    col = int(bot_move[1])
    return row, col-1

# Player
def player(used_coordinates, coordinates):
    user_input = validate()
    row = int(coordinates_dict[user_input[0]])
    col = int(user_input[1])
    return row, col-1

# Exit Game
def quit_game(user_input):
    if user_input.upper() == "QUIT":
        print("Goodbye")
        exit()


# 
def get_player_board_position():
    row = input("Enter a ship row: ", row_selected)
    while row not in row_selected:
        print("Please enter a valid row")
        row = input("Enter a ship row: ", row_selected)
    col = input("Enter a ship row: ", col_selected)
    while col not in col_selected:
        print("Please enter a valid col")
        col = input("Enter a ship row: ", col_selected)


def ask_for_ship(board):
    for ship in range(5):
        print("Enter your ships positions: ", ship + 1)
        row_selected, col_selected = get_player_board_position()
        if board[row_selected][col_selected] == "X":
            print("This spot is occupied by batleship. Please spot again: ", ship + 1)
        else:
            board[row_selected][col_selected] = "X"
            print(board)


def set_of_coordinates(row_selected, col_selected):
    options_to_choose = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
     "1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9}
    row = options_to_choose[row_selected]
    col = options_to_choose[col_selected]
    return row, col


def select_coordinates(board, row, col):
    cell_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    row_selected = input("Select a letter ").upper()
    col_selected = input("Select a number ")
    if row_selected and col_selected in cell_list:
        row, col = set_of_coordinates(row_selected, col_selected)
        return row, col
    else:
        print("Invalid input! You must select a cell on the board")
        select_coordinates(board, row, col)
        
def mark():  # Magda
    pass


def clear():  # NIKT
    os.system('cls' if os.name == 'nt' else 'clear')


def win():  # Magda
    pass


def validate(board):  # Vładek
    pass





def shooting_phase(board, row, col, height, width):  # Vładek
    board_for_note_player_1 = generation_board(height, width)
    board_for_note_player_2 = generation_board(height, width)
    select_coordinates(board, row, col)
    if board_player_1[row][col] == '.':
        board_for_note_player_1[row][col] == 'M'
        print("You've missed!")
        print_board(board_for_note_player_1)
    elif board_player_1[row][col] == 'X':
        board_for_note_player_1[row][col] == 'H'
        print("You've hit a ship!")
        print_board(board_for_note_player_1)
    if board_player_2[row][col] == '.':
        board_for_note_player_1[row][col] == 'M'
        print("You've missed!")
        print_board(board_for_note_player_2)
    elif board_player_2[row][col] == 'X':
        board_for_note_player_1[row][col] == 'H'
        print("You've hit a ship!")
        print_board(board_for_note_player_2)


def battleship():
    pass


def size_of_the_board():
    print('    Select board size:\n')
    size = input('''    1 = Board size 5x5
    2 = Board size 10x10 \n
    Your choice: ''')
    clear()
    if size == '1':
        board = generation_board(5, 5)
        print_board5_5(board)
    elif size == '2':
        board = generation_board(10, 10)
        print_board10_10(board)
    else:
        print('Choose one of the following options!!!')
        size_of_the_board()


def main_menu():
    size_of_the_board()
    ask_for_ship()
    clear()
    print("Spot your batleship")
    ask_for_ship()
    clear()
    get_player_board_position()


if __name__ == "__main__":
    main_menu()
