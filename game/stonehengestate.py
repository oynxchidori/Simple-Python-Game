"""Game State module for stonehenge"""

from game_state import GameState


class StonehengeState(GameState):
    """
    StonehengeState keeps track of all the informtion when two players
    play the StonehengeState.

    size: an integer indicating the size of board used to play StonehengeState
    turn: an integer keeping track of which player should act now
    right: a list keeping track of the right ley lines
    left: a list keeping track of the left ley lines
    down: a list keeping track of the down ley lines
    mov_list: a list keeping track of the current available moves
    """

    def __init__(self, is_p1_turn: bool, size: str) -> None:
        """
        Initialize a new Stonehenge state. It overrides the __init__ method
        in GameState.

        >>> a = StonehengeState(True, '2')
        >>> a.turns == 0
        True
        >>> a.size == '2'
        True
        """
        if is_p1_turn:
            self.turns = 0
        else:
            self.turns = 1
        self.size = size
        if int(self.size) == 5:
            self.right = [['@', 'A', 'C', 'F', 'J', 'O'],
                          ['@', 'B', 'D', 'G', 'K', 'P', 'U'],
                          ['@', 'E', 'H', 'L', 'Q', 'V'],
                          ['@', 'I', 'M', 'R', 'W'],
                          ['@', 'N', 'S', 'X'], ['@', 'T', 'Y']]
            self.down = [['@', 'T', 'N', 'I', 'E', 'B'],
                         ['@', 'Y', 'S', 'M', 'H', 'D', 'A'],
                         ['@', 'X', 'R', 'L', 'G', 'C'],
                         ['@', 'W', 'Q', 'K', 'F'],
                         ['@', 'V', 'P', 'J'], ['@', 'U', 'O']]
            self.left = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],
                         ['@', 'F', 'G', 'H', 'I'],
                         ['@', 'J', 'K', 'L', 'M', 'N'],
                         ['@', 'O', 'P', 'Q', 'R', 'S', 'T'],
                         ['@', 'U', 'V', 'W', 'X', 'Y']]
        elif int(self.size) == 4:
            self.right = [['@', 'A', 'C', 'F', 'J'],
                          ['@', 'B', 'D', 'G', 'K', 'O'],
                          ['@', 'E', 'H', 'L', 'P'], ['@', 'I', 'M', 'Q'],
                          ['@', 'N', 'R']]
            self.down = [['@', 'N', 'I', 'E', 'B'],
                         ['@', 'R', 'M', 'H', 'D', 'A'],
                         ['@', 'Q', 'L', 'G', 'C'],
                         ['@', 'P', 'K', 'F'], ['@', 'O', 'J']]
            self.left = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],
                         ['@', 'F', 'G', 'H', 'I'],
                         ['@', 'J', 'K', 'L', 'M', 'N'],
                         ['@', 'O', 'P', 'Q', 'R']]
        elif int(self.size) == 3:
            self.right = [['@', 'A', 'C', 'F'], ['@', 'B', 'D', 'G', 'J'],
                          ['@', 'E', 'H', 'K'], ['@', 'I', 'L']]
            self.down = [['@', 'I', 'E', 'B'], ['@', 'L', 'H', 'D', 'A'],
                         ['@', 'K', 'G', 'C'], ['@', 'J', 'F']]
            self.left = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'],
                         ['@', 'F', 'G', 'H', 'I'], ['@', 'J', 'K', 'L']]
        elif int(self.size) == 2:
            self.right = [['@', 'A', 'C'], ['@', 'B', 'D', 'F'],
                          ['@', 'E', 'G']]
            self.down = [['@', 'E', 'B'], ['@', 'G', 'D', 'A'], ['@', 'F', 'C']]
            self.left = [['@', 'A', 'B'], ['@', 'C', 'D', 'E'], ['@', 'F', 'G']]
        elif int(self.size) == 1:
            self.right = [['@', 'A'], ['@', 'B', 'C']]
            self.down = [['@', 'B'], ['@', 'C', 'A']]
            self.left = [['@', 'A', 'B'], ['@', 'C']]
        self.mov_list = []
        for x in self.right:
            for y in x:
                if y.isalpha():
                    self.mov_list.append(y)
        for x in self.down:
            for y in x:
                if y.isalpha():
                    self.mov_list.append(y)
        for x in self.left:
            for y in x:
                if y.isalpha():
                    self.mov_list.append(y)
        self.mov_list = set(self.mov_list)
        self.mov_list = list(self.mov_list)
        self.mov_list.sort()

    def __str__(self) -> str:
        """
        Return a string representation of StonehengeState.
        """
        if int(self.size) == 5:
            return '              {}   {}\n             /   /\n      ' \
                   '  {} - {} - {}   {}\n           / \\ / \\ /\n    ' \
                   '  {} - {} - {} - {}   {}\n         / \\ / \\ / \\ /\n   ' \
                   ' {} - {} - {} - {} - {}   {}\n       / \\ / \\ / \\ ' \
                   '/ \\ /\n  {} - {} - {} - {} - {} - {}   {}\n     / \\' \
                   ' / \\ / \\ / \\ / \\ /\n{} - {} - {} - {} - {} - {} -' \
                   ' {}\n     \\ / \\ / \\ / \\ / \\ / \\\n  {} - {} - {}' \
                   ' - {} - {} - {}   {}\n       \\ ' \
                   '  \\   \\   \\   \\\n        {}   {}   {}   {}   {}\n'.\
                format(self.right[0][0], self.right[1][0], self.left[0][0],
                       self.mov_list[0], self.mov_list[1], self.right[2][0],
                       self.left[1][0], self.mov_list[2], self.mov_list[3],
                       self.mov_list[4], self.right[3][0], self.left[2][0],
                       self.mov_list[5], self.mov_list[6], self.mov_list[7],
                       self.mov_list[8], self.right[4][0], self.left[3][0],
                       self.mov_list[9], self.mov_list[10], self.mov_list[11],
                       self.mov_list[12], self.mov_list[13], self.right[5][0],
                       self.left[4][0], self.mov_list[14], self.mov_list[15],
                       self.mov_list[16], self.mov_list[17], self.mov_list[18],
                       self.mov_list[19], self.left[5][0], self.mov_list[20],
                       self.mov_list[21], self.mov_list[22], self.mov_list[23],
                       self.mov_list[24], self.down[0][0], self.down[5][0],
                       self.down[4][0], self.down[3][0], self.down[2][0],
                       self.down[1][0])
        elif int(self.size) == 4:
            return '            {}   {}\n           /   /\n      {} - {} - {}' \
                   '   {}\n         / \\ / \\ /\n    {} - {} - {} - {}   ' \
                   '{}\n       / \\ / \\ / \\ /\n  {} - {} - {} - {} - {}' \
                   '   {}\n     / \\ / \\ / \\ / \\ /\n{} - {} - {} - {}' \
                   ' - {} - {}\n     \\ / \\ / \\ / \\ / \\\n  {} - {} -' \
                   ' {} - {} - {}   {}\n       \\   \\   \\   \\\n       ' \
                   ' {}   {}   {}   {}\n'.\
                format(self.right[0][0], self.right[1][0], self.left[0][0],
                       self.mov_list[0], self.mov_list[1], self.right[2][0],
                       self.left[1][0], self.mov_list[2], self.mov_list[3],
                       self.mov_list[4], self.right[3][0], self.left[2][0],
                       self.mov_list[5], self.mov_list[6], self.mov_list[7],
                       self.mov_list[8], self.right[4][0], self.left[3][0],
                       self.mov_list[9], self.mov_list[10], self.mov_list[11],
                       self.mov_list[12], self.mov_list[13], self.left[4][0],
                       self.mov_list[14], self.mov_list[15], self.mov_list[16],
                       self.mov_list[17], self.down[0][0], self.down[4][0],
                       self.down[3][0], self.down[2][0], self.down[1][0])
        elif int(self.size) == 3:
            return '          {}   {}\n         /   /\n    {} - {} - {}' \
                   '   {}\n       / \\ / \\ /\n  {} - {} - {} - {}   {}\n' \
                   '     / \\ / \\ / \\ /\n{} - {} - {} - {} - {}\n     ' \
                   '\\ / \\ / \\ / \\\n  {} - {} - {} - {}   {}\n       ' \
                   '\\   \\   \\\n        {}  ' \
                   ' {}   {}\n'.format(self.right[0][0], self.right[1][0],
                                       self.left[0][0], self.mov_list[0],
                                       self.mov_list[1], self.right[2][0],
                                       self.left[1][0], self.mov_list[2],
                                       self.mov_list[3], self.mov_list[4],
                                       self.right[3][0], self.left[2][0],
                                       self.mov_list[5], self.mov_list[6],
                                       self.mov_list[7], self.mov_list[8],
                                       self.left[3][0], self.mov_list[9],
                                       self.mov_list[10], self.mov_list[11],
                                       self.down[0][0], self.down[3][0],
                                       self.down[2][0], self.down[1][0])
        elif int(self.size) == 2:
            return '        {}   {}\n       /   /\n  {} - {} - {}   {}\n    ' \
                   ' / \\ / \\ /\n{} - {} - {} - {}\n     \\ / \\ / \\\n ' \
                   ' {} - {} - {}   {}\n       \\   \\\n        {}   {}'.\
                format(self.right[0][0], self.right[1][0], self.left[0][0],
                       self.mov_list[0], self.mov_list[1], self.right[2][0],
                       self.left[1][0], self.mov_list[2], self.mov_list[3],
                       self.mov_list[4], self.left[2][0], self.mov_list[5],
                       self.mov_list[6], self.down[0][0], self.down[2][0],
                       self.down[1][0])
        return '      {}   {}\n     /   /\n{} - {} - {}\n     \\ / \\\n ' \
            ' {} - {}   {}\n       \\\n        {}'.\
            format(self.right[0][0], self.right[1][0], self.left[0][0],
                   self.mov_list[0], self.mov_list[1], self.left[1][0],
                   self.mov_list[2], self.down[0][0], self.down[1][0])

    def get_current_player_name(self) -> str:
        """
        Return the name of the current player. It overrides the
        get_current_player_name method in superclass game_state.

        >>> p = StonehengeState(True, '1')
        >>> p.get_current_player_name()
        'p1'
        """
        if self.turns % 2 == 0:
            return 'p1'
        return 'p2'

    def get_possible_moves(self) -> list:
        """Return all the possible moves that current player could make. It
        overrides the get_possible_moves mehod in superclass GameState.

        >>> p = StonehengeState(True, '1')
        >>> p.get_possible_moves()
        ['A', 'B', 'C']
        """
        sum1, sum2 = 0, 0
        for x in self.right:
            if x[0] == 1:
                sum1 += 1
            elif x[0] == 2:
                sum2 += 1
        for x in self.down:
            if x[0] == 1:
                sum1 += 1
            elif x[0] == 2:
                sum2 += 1
        for x in self.left:
            if x[0] == 1:
                sum1 += 1
            elif x[0] == 2:
                sum2 += 1
        if sum1 >= len(self.right) * 3 * 0.5 or \
                sum2 >= len(self.right) * 3 * 0.5:
            return []
        return [x for x in self.mov_list if type(x) == str]

    def make_move(self, move: str) -> 'StonehengeState':
        """
        Return a new state of the game Stonehenge after executing a move. It
        overrides the make_move method in superclass game_state.

        >>> p = StonehengeState(True, '1')
        >>> p1 = p.make_move('A')
        >>> p1.get_possible_moves()
        []
        """
        other = StonehengeState(self.turns % 2 == 0, self.size)
        other.size, other.mov_list, other.turns = \
            self.size, self.mov_list[:], self.turns
        other.right = [[x] for x in range(len(self.right))]
        other.left = [[x] for x in range(len(self.left))]
        other.down = [[x] for x in range(len(self.down))]
        for x in range(len(self.right)):
            other.right[x], other.left[x], other.down[x] = \
                self.right[x][:], self.left[x][:], self.down[x][:]
        for x in other.right:
            for y in range(len(x)):
                if x[y] == move and other.turns % 2 == 0:
                    other.mov_list[other.mov_list.index(x[y])] = 1
                    x[y] = 1
                elif x[y] == move and other.turns % 2 != 0:
                    other.mov_list[other.mov_list.index(x[y])] = 2
                    x[y] = 2
        for x in other.down:
            for y in range(len(x)):
                if x[y] == move and other.turns % 2 == 0:
                    x[y] = 1
                elif x[y] == move and other.turns % 2 != 0:
                    x[y] = 2
        for x in other.left:
            for y in range(len(x)):
                if x[y] == move and other.turns % 2 == 0:
                    x[y] = 1
                elif x[y] == move and other.turns % 2 != 0:
                    x[y] = 2
        for x in other.right:
            if x.count(1) >= 0.5 * (len(x) - 1) and 1 in x and x[0] == '@':
                x[0] = 1
            elif x.count(2) >= 0.5 * (len(x) - 1) and 2 in x and x[0] == '@':
                x[0] = 2
        for x in other.down:
            if x.count(1) >= 0.5 * (len(x) - 1) and 1 in x and x[0] == '@':
                x[0] = 1
            elif x.count(2) >= 0.5 * (len(x) - 1) and 2 in x and x[0] == '@':
                x[0] = 2
        for x in other.left:
            if x.count(1) >= 0.5 * (len(x) - 1) and 1 in x and x[0] == '@':
                x[0] = 1
            elif x.count(2) >= 0.5 * (len(x) - 1) and 2 in x and x[0] == '@':
                x[0] = 2
        other.turns += 1
        return other

    def is_valid_move(self, move: str) -> bool:
        """
        Return whether the input move is a valid move. It overrides the
        is_valid_move method in superclass game_state.

        >>> p = StonehengeState(True, '1')
        >>> p.is_valid_move('A')
        True
        >>> p.is_valid_move('1')
        False
        """
        return move in self.mov_list

    def __repr__(self) -> str:
        """
        Return a representation of the current game state. It overrides the
        __repr__ method in superclass game_state.
        """
        if self.turns % 2 == 0:
            p = 'p1'
        else:
            p = 'p2'
        return 'The current game board becomes: \n' + \
               StonehengeState.__str__(self) + '\nThe current player is: ' \
               + p + '\nThe current available moves are: ' + \
               str(self.get_possible_moves())

    def rough_outcome(self) -> float:
        """
        Return a rough estimate in the interval [LOSE, WIN] to predict the
        best outcome of the current player according to the current state.

        >>> p = StonehengeState(True, '1')
        >>> p.rough_outcome()
        1
        """
        if any([self.make_move(a).get_possible_moves() == []
                for a in self.get_possible_moves()]):
            return self.WIN
        if self.get_possible_moves() == []:
            return self.LOSE
        trutable = []
        for y in self.get_possible_moves():
            for z in self.make_move(y).get_possible_moves():
                t = self.make_move(y).make_move(z).get_possible_moves() == []
                trutable.append(t)
        if all([trutable]):
            return self.LOSE
        return self.DRAW


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
