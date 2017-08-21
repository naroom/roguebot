import random

from roguebot.constants import (
    MONSTER_CHARS,
    DIRECTION_KEYS,
    WALL_CHARS
)
from roguebot.interface.frame_parser import get_adjacent

from roguebot.util import flatten

'''
Really dumb bot that attacks monsters, moves randomly, and goes down stairs.

Sort of viable, if starvation is disabled and it's given a lot of attempts.
'''



def get_move(frames, stats):
    # go down stairs, if we happen to hit any
    # Stupid, so can trigger if monster walks over stairs too.
    if '%' in frames[1] and '%' not in frames[0]:
        return '>'

    if random.random() < 0.05:
        # small chance of making a random move, gets out of odd 'stuck' situations
        return 'C-' + random.choice(flatten(DIRECTION_KEYS))

    adj = get_adjacent(frames[0])  # 3x3 matrix with @ in center

    for row_idx, row in enumerate(adj):
        for col_idx, char in enumerate(row):
            if char in MONSTER_CHARS:
                move_towards_monster = DIRECTION_KEYS[row_idx][col_idx]
                return fix_diagonal(move_towards_monster, adj)

    # OK, just move randomly
    if random.random() < 0.1:
        # chance to search
        return 's'
    else:
        return 'C-' + random.choice(flatten(DIRECTION_KEYS))


def fix_diagonal(move, adj):
    """
    Can't move diagonally if there's a wall in the way, e.g:
         ..|
         .@|
         ..E#####
    We can't attack that emu. Do the best we can in this scenario instead.
    """
    # up-right
    if move == DIRECTION_KEYS[0][2] and adj[0][1] in WALL_CHARS:
        return DIRECTION_KEYS[1][2]
    if move == DIRECTION_KEYS[0][2] and adj[1][2] in WALL_CHARS:
        return DIRECTION_KEYS[0][1]

    # up-left
    if move == DIRECTION_KEYS[0][0] and adj[0][1] in WALL_CHARS:
        return DIRECTION_KEYS[1][0]
    if move == DIRECTION_KEYS[0][0] and adj[1][0] in WALL_CHARS:
        return DIRECTION_KEYS[0][1]

    # down-left
    if move == DIRECTION_KEYS[2][0] and adj[2][1] in WALL_CHARS:
        return DIRECTION_KEYS[1][0]  # wall down so go left
    if move == DIRECTION_KEYS[2][0] and adj[1][0] in WALL_CHARS:
        return DIRECTION_KEYS[2][1]  # wall left so go down

    # down-right
    if move == DIRECTION_KEYS[2][2] and adj[2][1] in WALL_CHARS:
        return DIRECTION_KEYS[1][2]  # wall down so go right
    if move == DIRECTION_KEYS[2][2] and adj[1][2] in WALL_CHARS:
        return DIRECTION_KEYS[2][1]  # wall right so go down

    # none of the above, the diagonal is fine
    return move