import os
def generation_board(height,width):  # Sebastian
    board = []
    for i in range(height):
        board.append(['.'] * width)
    return board

def print_board(board):  # Sebastian
    pass


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


if __name__ == "__main__":
    print(generation_board(5,5))
