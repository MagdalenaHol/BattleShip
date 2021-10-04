import os
def generation_board(height,width): 
    board = []
    for i in range(height):
        board.append(['.'] * width)
    return board

def print_board5_5(board):
    a = 0
    print('        A B C D E ')
    print('        v v v v v ')
    print('       ___________')
    for element in board:
        a += 1
        b = str(a)
        element = ' '.join(element)
        print(b.rjust(2),"=>","|", element,"|")
    print('       -----------') 
    return board

def print_board10_10(board):
    a = 0
    print('        A B C D E F G H I J')
    print('        v v v v v v v v v v')
    print('       ____________________')
    for element in board:
        a += 1
        b = str(a)
        element = ' '.join(element)
        print(b.rjust(2),"=>","|", element,"|")
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


def validate():  # Vładek
    pass


def shooting_phase():  # Vładek
    pass


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
    