class Player:
    """
    Represents a player in the Tic-Tac-Toe game.
    """
    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol


class TicTacToe:
    """
    Manages the state and logic of a Tic-Tac-Toe game.
    """
    WIN_COMBINATIONS = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]

    def __init__(self):
        # Initialize an empty board
        self.board = [' '] * 9
        # Create two players
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player = self.players[0]

    def display_board(self) -> None:
        """Prints the current state of the board."""
        print('\n')
        for row in range(3):
            print(' | '.join(self.board[row*3:(row+1)*3]))
            if row < 2:
                print('--+---+--')
        print('\n')

    def switch_player(self) -> None:
        """Switches turn to the other player."""
        idx = self.players.index(self.current_player)
        self.current_player = self.players[1 - idx]

    def make_move(self, position: int) -> bool:
        """
        Attempts to place the current player's symbol at the given position (1-9).
        Returns True if move was successful, False otherwise.
        """
        if position < 1 or position > 9:
            print("Invalid position. Choose a number between 1 and 9.")
            return False
        if self.board[position - 1] != ' ':
            print("That spot is already taken. Try again.")
            return False
        self.board[position - 1] = self.current_player.symbol
        return True

    def check_win(self) -> bool:
        """Checks if the current player has won the game."""
        b = self.board
        sym = self.current_player.symbol
        for combo in TicTacToe.WIN_COMBINATIONS:
            if all(b[i] == sym for i in combo):
                return True
        return False

    def check_draw(self) -> bool:
        """Checks if the game is a draw (board full, no winner)."""
        return all(space != ' ' for space in self.board)

    def play(self) -> None:
        """Runs the main game loop."""
        print("Welcome to Tic-Tac-Toe!")
        while True:
            self.display_board()
            try:
                choice = int(input(f"{self.current_player.name} ({self.current_player.symbol}), choose your move (1-9): "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if not self.make_move(choice):
                continue

            if self.check_win():
                self.display_board()
                print(f"Congratulations {self.current_player.name}! You win!")
                break

            if self.check_draw():
                self.display_board()
                print("It's a draw!")
                break

            self.switch_player()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
