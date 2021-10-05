import os
import random


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


# logic ai Player
def ai_player(coordinates):
    bot_move = random.choice(coordinates)
    coordinates.remove(bot_move)
    row = int(coordinates_dict[bot_move[0]])
    col = int(bot_move[1])
    return row, col-1

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


def ask_for_ship(board):
    for ship in range(5):
        print("Enter your ships positions: ", ship + 1)
        row_selected, col_selected = select_coordinates()
        if board[row_selected][col_selected] == "X":
            print("This spot is occupied by batleship. Please spot again: ", ship + 1)
        else:
            board[row_selected][col_selected] = "X"
            print(board)
       
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

def quit_game(user_input):
    if user_input.upper() == "QUIT":
        print("Goodbye")
        exit()
def battleship():
    pass


def size_of_the_board():
    print('    Select board size')
    size = int(input('Specify the map size from 5 to 10: '))
    if size >= 5 and size <=10:
        return size
    else:
        print('Wrong map size, please enter corect map size!')
        size_of_the_board()


def main_menu():
    size_of_the_board()
    size = size_of_the_board()
    board = generation_board(size)
    ask_for_ship()
    clear()
    print("Spot your batleship")
    ask_for_ship()
    clear()


if __name__ == "__main__":
    main_menu()
