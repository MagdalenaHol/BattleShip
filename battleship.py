import os

def generation_board(height, width): 
    board = []
    for i in range(height):
        board.append(['.'] * width)
    return board

def print_board5_5(board):
    char = 0
    print('        1 2 3 4 5 ')
    print('        v v v v v ')
    print('       ___________')
    for element in board:
        char += 1
        element = ' '.join(element)
        print(chr(char + 64).rjust(2),"=>","|", element,"|")
    print('       -----------') 
    return board

def print_board10_10(board):
    char = 0
    print('        1 2 3 4 5 6 7 8 9 10')
    print('        v v v v v v v v v v')
    print('       ____________________')
    for element in board:
        char += 1
        element = ' '.join(element)
        print(chr(char + 64).rjust(2),"=>","|", element,"|")
    print('       --------------------') 


def ai_player():  # Denys
    pass


def player():  # Denys
    pass


def mark():  # Magda
    pass


def clear():  # NIKT
    os.system('cls' if os.name == 'nt' else 'clear')

def win():  # Magda
    pass


def validate(board):  # Vładek
    pass


def set_of_coordinates(row_selected, col_selected): 
    options_to_choose = {"A": 0, "B": 1, "C": 2,"D ": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9,
     "1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9}
    row = options_to_choose[row_selected]
    col = options_to_choose[col_selected]
    return row, col

def select_coordinates(board, row, col):
    cell_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    row_selected = input("Select a cell ").upper()
    col_selected = input("Select a cell ")
    if row_selected and col_selected in cell_list:
        row, col = set_of_coordinates(row_selected, col_selected)
    else:
        print("Invalid input! You must select a cell on the board")
        select_coordinates(board, row, col)

def shooting_phase(board, row, col,height,width):  # Vładek
    board_for_note_player_1 = generation_board(height,width)
    board_for_note_player_2 = generation_board(height,width)
    select_coordinates(board, row, col)
    if board_player_1[row][col] == '.':
        board_for_note_player_1[row][col] == 'M'
        print("You've missed!")
        print_board(board_for_note_player_1)
    elif board_player_1[row][col] == 'X':
        board_for_note_player_1[row][col] == 'H'
        print("You've hit a ship!")
        print_board(board_for_note_player_1)
    if  board_player_2[row][col] == '.':
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
        board = generation_board(5,5)
        print_board5_5(board)
    elif size == '2':
        board = generation_board(10,10)
        print_board10_10(board)
    else:
        print('Choose one of the following options!!!')
        size_of_the_board()
def main_menu():
    size_of_the_board()
    

if __name__ == "__main__":
    main_menu()
    