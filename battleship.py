import os
def generation_board(height,width): 
    board = []
    for i in range(height):
        board.append(['.'] * width)
    return board

def print_board(board):
    for element in board:
        element = ' '.join(element)
        print(element)
        


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

def main_menu():
    pass

if __name__ == "__main__":
    board = generation_board(5,5)
    print_board(board)