from utility import write, ALPHA, BETA
from typing import List
import sys
import numpy as np


def insert(s: str, char: str, i: int):
    """
    Insert char to str s at index i
    """
    return s[:i] + char + s[i:]


def replace(s: str, char: str, i: int):
    return s[:i] + char + s[i + 1:]


def backtrack(s: str, t: str, table: List[List[int]]):
    """
    Backtrack the alignment given the 2d table
    """
    m, n = len(s), len(t)
    while m or n:
        i = np.argmin([BETA + table[m][n - 1] if n else float('inf'),
                       BETA + table[m - 1][n] if m else float('inf'),
                       ALPHA[s[m - 1]][t[n - 1]] + table[m - 1][n - 1] if m and n else float('inf')])
        if i == 0:
            s = insert(s, '_', m)
            n -= 1
        elif i == 1:
            t = insert(t, '_', n)
            m -= 1
        else:
            # s = replace(s, t[n - 1], m - 1)
            m -= 1
            n -= 1
    return s, t


def sequence_alignment_basic(s: str, t: str):
    """
    Implement the basic dp version sequence alignment algorithm

    Args:
        s: sequence s
        t: sequence t

    Returns:
        the cost of alignment, sequence s, sequence t after alignment
    """
    m, n = len(s), len(t)
    # opt(i, j): min cost between s[0:i] to t[0:j]
    table = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, n + 1):
        table[0][i] = BETA * i
    for j in range(1, m + 1):
        table[j][0] = BETA * j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            table[i][j] = min(BETA + table[i][j - 1], BETA + table[i - 1][j],
                              ALPHA[s[i - 1]][t[j - 1]] + table[i - 1][j - 1])

    _s, _t = backtrack(s, t, table)
    return table[m][n], _s, _t


if __name__ == '__main__':
    write(sequence_alignment_basic, sys.argv[1])
