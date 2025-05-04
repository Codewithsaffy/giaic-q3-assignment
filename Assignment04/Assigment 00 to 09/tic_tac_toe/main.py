class Player:
    def __init__(self, name:str, symbol:str):
        self.name = name
        self.symbol = symbol


class TicTacToe:
    WIN_COMBINATION = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    def __init__(self):
        self.board = [' ']*9
        self.players = [Player("player 1", "X"), Player("player 2", "Y")]
        self.current_player = self.players[0]
    
    def display_board(self):
        print("\n")
        for row in range(3):
            print(" | ".join(self.board[row*3:(row+1)*3]))
            if row < 2:
                print('--+---+--')
        print("\n")

    def switch_player(self):
        idx = self.players.index(self.current_player)
        self.current_player = self.players[1 - idx]
        
    def make_move(self, position:int):
        if position < 1 or position > 9:
            print("Invalid position. Choose a number between 1 and 9.")
            return False
        if self.board[position - 1] != ' ':
            print("That spot is already taken. Try again.")
            return False
        self.board[position - 1] = self.current_player.symbol
        return True
    


