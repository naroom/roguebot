import random

"""
Determines move direction from a neural network.

"""


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
