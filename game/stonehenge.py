"""Game Module Stonehenge"""
from game import Game
from stonehengestate import StonehengeState


class StonehengeGame(Game):
    """Stonehenge is a game played by two players and proceeds according to the
    players' input.

    size: an integer determining the size of the board.
    current_state: the current state of the game
    """

    def __init__(self, p1_starts: bool) -> None:
        """Initialize a new StoneHenge Game. It overrides the __init__ method
        in superclass Game.
        """
        self.size = input('Input an integer to determine the size of board: ')
        self.current_state = StonehengeState(p1_starts, self.size)

    def get_instructions(self) -> str:
        """Return the instruction for playing Stonehenge.
        """
        return 'Stonehenge is a two-player game which proceeds by players' \
               ' inputting different letters in each turn. In the beginning,' \
               ' the size of the board for a new stonehenge game is ' \
               'determined and the board has the number of rows that ' \
               'is equal to size adding one. The letters are connected ' \
               'by ley-lines in order and players are required to input ' \
               'letters in each turn. When a player has inputted at least' \
               ' half of the letters on a ley-line, the player claims this' \
               ' line. The first player who successfully claims half of ' \
               'the ley-lines is the winner.'

    def is_over(self, state: 'StonehengeState') -> bool:
        """Return whether a new game Stonehenge is finished.
        """
        count1, count2 = sum([1 for a in state.right if a[0] == 1]), \
            sum([1 for a in state.right if a[0] == 2])
        count11, count22 = sum([1 for a in state.down if a[0] == 1]), \
            sum([1 for a in state.down if a[0] == 2])
        count111, count222 = sum([1 for a in state.left if a[0] == 1]), \
            sum([1 for a in state.left if a[0] == 2])
        return ((count1 + count11 + count111) >= 0.5 * len(state.right) * 3) \
            or ((count2 + count22 + count222) >= 0.5 * len(state.right) * 3)

    def is_winner(self, player: str) -> bool:
        """Return whether the player is the winner of the current game.
        """
        if self.is_over(self.current_state):
            count1, count2 = \
                sum([1 for a in self.current_state.right if a[0] == 1]), \
                sum([1 for a in self.current_state.right if a[0] == 2])
            count11, count22 = \
                sum([1 for a in self.current_state.down if a[0] == 1]), \
                sum([1 for a in self.current_state.down if a[0] == 2])
            count111, count222 = \
                sum([1 for a in self.current_state.left if a[0] == 1]), \
                sum([1 for a in self.current_state.left if a[0] == 2])
            if player == 'p1':
                return (count1 + count11 + count111) >= \
                    0.5 * len(self.current_state.right) * 3
            elif player == 'p2':
                return (count2 + count22 + count222) >= \
                    0.5 * len(self.current_state.right) * 3
        return False

    def str_to_move(self, string: str) -> str:
        """
        Return the move that string represents in correct type if the move
        is legal; otherwise returns invalid input.
        """
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if string in alpha:
            return string
        return 'invalid move'


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
