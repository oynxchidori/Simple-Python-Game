"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
from typing import Any
import copy
from game import Game


def interactive_strategy(game: Any) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move


def compila(list_: list) -> list:
    """
    Return a list of integers where every element that is originally a
    list becomes not a list. Similar to the flatten function we learned in
    class.
    """
    if not isinstance(list_, list):
        return [list_]
    return sum([compila(l) for l in list_], [])


def track_move(game: Game, player: str) -> Any:
    """
    Return an expected list of outcomes.
    """
    if game.is_over(game.current_state):
        if game.is_winner('p1') and player == 'p1':
            return 1
        if game.is_winner('p1') and player != 'p1':
            return -1
        if game.is_winner('p2') and player == 'p2':
            return 1
        if game.is_winner('p2') and player != 'p2':
            return -1
        if not game.is_winner('p1') and not game.is_winner('p2'):
            return 0
    save = game.current_state
    t = []
    for m in game.current_state.get_possible_moves():
        game.current_state = game.current_state.make_move(m)
        t1 = track_move(game, player)
        t1 = compila(t1)
        if len(t1) > 1:
            t1 = max(t1)
        t.append(t1)
        game.current_state = save
    return t


def recursive_minimax(game: Game) -> Any:
    """
    A strategy that returns any type representing the moves of the game and
    determines the current best action for players by using recursion.
    """
    haha = track_move(game, game.current_state.get_current_player_name())
    haha = compila(haha)
    re = game.current_state.get_possible_moves()[haha.index(max(haha))]
    detect = []
    for x in game.current_state.get_possible_moves():
        g1 = copy.deepcopy(game)
        g1.current_state = g1.current_state.make_move(
            game.str_to_move(str(x)))
        f = track_move(g1, game.current_state.get_current_player_name())
        f = compila(f)
        detect.append(f)
    for x in range(len(detect)):
        if all([y == 1 for y in detect[x]]):
            re = game.current_state.get_possible_moves()[x]
    if type(re) != str:
        re = str(re)
    return game.str_to_move(re)


class Gamechain:
    """
    A type that temporaily keeps tracks of the next moves that are available
    according to the current moves and it is used by the iterative minimax
    strategy.

    game: the game that is chained
    children: a list keeping track of the reachable states that are reachable
    from the current state.
    score: an int indicate the score of the current state.
    """

    def __init__(self, game: Game) -> None:
        """
        Initialize a new Gamechain.
        """
        self.game, self.children, self.score = game, [], None

    def __eq__(self, other: 'Gamechain') -> bool:
        """
        Return whether self is equal to other by checking their internal
        information.
        """
        return self.game.current_state.__repr__() == \
               other.game.current_state.__repr__()


def fliter(game: 'Game', lis: list) -> None:
    """
    Put all the states that are reachable from the the current state in front
    of the list lis.
    """
    prepare = game.current_state.get_possible_moves()[:]
    count = len(game.current_state.get_possible_moves())
    while count != 0:
        save = copy.deepcopy(game)
        save1 = save.current_state.make_move(prepare[0])
        save.current_state = save1
        lis.insert(0, Gamechain(save))
        prepare.remove(prepare[0])
        count -= 1


def helper_to_return(gam: Game, move_con: 'Gamechain', list1: list) -> Any:
    """
    Return a move for the game after satisfying certain conditions by checking
    list1, list2 and list3.
    """
    for x in list1:
        if gam.current_state.make_move(x).__repr__() == \
                move_con.game.current_state.__repr__():
            return gam.str_to_move(x)
    return '.'


def helper_prep(list1: list, node: Any) -> None:
    """
    A helper funtion used to assist for preparing iterative minimax.
    """
    for x in list1[:list1.index(node)]:
        if x is not None and x != node:
            list1[list1.index(node)].children.append(x)


def iterative_minimax(game: Game) -> Any:
    """
    A strategy that returns any type representing the moves of the game and
    determines the current best action for players by using traditional
    iterative methods.
    """
    list_, store = [Gamechain(game)], []
    while len(list_) != 0:
        if list_[0].children == [] and \
                not list_[0].game.is_over(list_[0].game.current_state):
            te = copy.deepcopy(list_[0])
            fliter(list_[0].game, list_)
            helper_prep(list_, te)
            # for x in list_[:list_.index(te)]:
            #     if x is not None and x != te:
            #         list_[list_.index(te)].children.append(x)
        elif list_[0].children != [] or\
                list_[0].game.is_over(list_[0].game.current_state):
            if list_[0].game.is_over(list_[0].game.current_state) and \
                    (list_[0].game.is_winner('p1') or
                     list_[0].game.is_winner('p2')):
                list_[0].score = -1
            elif list_[0].game.is_over(list_[0].game.current_state) and \
                    not list_[0].game.is_winner('p1') and \
                    not list_[0].game.is_winner('p2'):
                list_[0].score = 0
            if list_[0].children != [] and \
                    all([x in store for
                         x in list_[0].children if x is not None]):
                list_[0].score = max([y.score * (-1) for y in store
                                      if y in list_[0].children])
            store.append(list_[0])
            list_.remove(list_[0])
    moves = [x for x in store if x in store[-1].children]
    move2 = game.current_state.get_possible_moves()
    for x in range(len(move2)):
        if type(move2[x]) != str:
            move2[x] = str(move2[x])
    for g in moves:
        if g.score == store[-1].score * (-1):
            return helper_to_return(game, g, move2)
    return '.'
    # for x in move2:
    #     if game.current_state.make_move(x).__repr__() == \
    #             g.game.current_state.__repr__():
    #         return game.str_to_move(x)


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
