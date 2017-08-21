def flatten(ls):
    """
    Convenience function to flatten a list of lists into one big list.
    [['a', 'b'], ['c', 'd']] -> ['a', 'b', 'c', 'd']
    """
    return sum(ls, [])
