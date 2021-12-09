from utility import write, ALPHA, BETA
from typing import List
from sequence_alignment_basic import sequence_alignment_basic
import sys
from functools import reduce


def sequence_alignment_helper(s: str, t: str) -> List[int]:
    """
    Dp version of sequence alignment with linear space. Only return the last row
    """
    m, n = len(s), len(t)
    table = [0] + [BETA * (i + 1) for i in range(n)]
    for i in range(1, m + 1):
        new_table = [BETA * i] + [0] * n
        for j in range(1, n + 1):
            new_table[j] = min(BETA + new_table[j - 1], BETA + table[j],
                               ALPHA[s[i - 1]][t[j - 1]] + table[j - 1])
        table = new_table
    return table


def sequence_alignment_efficient(s: str, t: str):
    """
    Memory efficient version of sequence alignment using divide & conquer and dynamic programming

    Args:
        s: sequence s
        t: sequence t

    Returns:
        the cost of alignment, sequence s, sequence t after alignment
    """
    if len(s) <= 2 or len(t) <= 2:
        return sequence_alignment_basic(s, t)
    m, n = len(s), len(t)
    mid = m >> 1
    arr1, arr2 = sequence_alignment_helper(s[:mid], t), sequence_alignment_helper(s[mid:][::-1], t[::-1])
    idx = reduce(lambda i, j: i if arr1[i] + arr2[n - i] <= arr1[j] + arr2[n - j] else j, range(n + 1))

    _, s_left, t_left = sequence_alignment_efficient(s[:mid], t[:idx])
    _, s_right, t_right = sequence_alignment_efficient(s[mid:], t[idx:])

    return arr1[idx] + arr2[n - idx], s_left + s_right, t_left + t_right


if __name__ == '__main__':
    write(sequence_alignment_efficient, sys.argv[1])
