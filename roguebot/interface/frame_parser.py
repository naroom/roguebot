def check_death(frame):
    return ("Killed" in frame or "starvation" in frame or 'hypothermia' in frame)


def check_victory(frame):
    return "great profit" in frame


def get_stats(frame):
    lines = frame.split('\n')
    lines[:]
    """
    Level: 99
    Gold: 999999
    Hp: 999(999)
    Str: 99(99)
    Arm: 99
    Exp: 21 / 10000000
    Hungry
    """
    pass


def check_more(frame):
    return '-more-' in frame


def get_line_char(line, pos, default):
    """
    rogue doesn't render the rightmost spaces on a line, which makes all the lines different lengths.
    That causes bounds checks to fail. :(
    So here's a getter with a providable default in case of bounds checks.
    """
    if pos >= len(line):
        return default
    else:
        return line[pos]

def get_adjacent(frame):
    """
    Return a list of the 8 positions adjacent to the player

    """

    adjacent = [
        [' ', ' ', ' '],
        [' ', '@', ' '],
        [' ', ' ', ' '],
    ]

    # note: @ would hit a wall before reaching the edge of the screen, so no bounds check needed there.
    lines = frame.split('\n')
    for linenum, line in enumerate(lines):
        if '@' in line:
            idx = line.find('@')

            adjacent[1][0] = get_line_char(line, idx - 1, ' ')  # left
            adjacent[1][2] = get_line_char(line, idx + 1, ' ')  # right

            above_line = lines[linenum - 1]
            adjacent[0][0] = get_line_char(above_line, idx - 1, ' ')
            adjacent[0][1] = get_line_char(above_line, idx, ' ')
            adjacent[0][2] = get_line_char(above_line, idx + 1, ' ')

            below_line = lines[linenum + 1]
            adjacent[2][0] = get_line_char(below_line, idx - 1, ' ')
            adjacent[2][1] = get_line_char(below_line, idx, ' ')
            adjacent[2][2] = get_line_char(below_line, idx + 1, ' ')

            break

    return adjacent