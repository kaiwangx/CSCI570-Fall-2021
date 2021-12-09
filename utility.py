from functools import reduce
import random
from typing import List
import timeit
import tracemalloc

ALPHA = {'A': {'A': 0, 'C': 110, 'G': 48, 'T': 94},
         'C': {'A': 110, 'C': 0, 'G': 118, 'T': 48},
         'G': {'A': 48, 'C': 118, 'G': 0, 'T': 110},
         'T': {'A': 94, 'C': 48, 'G': 110, 'T': 0}}

BETA = 30


def string_generator(base: str, indices: List[int]) -> str:
    """
    Generate the sequence base on the base string and indices.

    Args:
        base:  a string
        indices: a list of int

    Returns:
        The generated sequence
    """
    return str(reduce(lambda prev, idx: prev[:idx + 1] + prev + prev[idx + 1:], indices, base))


def to_int_array(arr: List[str]) -> List[int]:
    """
    Transform string arr to int arr. For example: ["1", "2", "3"] to [1, 2, 3]
    """
    return list(map(lambda x: int(x), arr))


def parse(filename: str) -> (str, str):
    """
    Parse the input file

    Returns:
        (sequence s, arr of indices), (sequence t, arr of indices)
    """
    with open(filename, 'r') as file:
        lines = list(map(lambda line: line.rstrip(), file.readlines()))
    [b1, b2] = list(filter(lambda idx: not lines[idx].isnumeric(), range(len(lines))))
    return string_generator(lines[b1], to_int_array(lines[1:b2])), string_generator(lines[b2],
                                                                                    to_int_array(lines[b2 + 1:]))


def find_cost(s: str, t: str) -> int:
    """
    Calculate the cost between sequence s and sequence t
    """
    return sum(BETA if s[i] == '_' or t[i] == '_' else ALPHA[s[i]][t[i]] for i in range(len(s)))


def write(func, arg):
    """
    Format and write result return by the func (basic/efficient)
    """
    with open('output.txt', "w") as f:
        s, t = parse(arg)
        tracemalloc.start()
        start = timeit.default_timer()
        cost, r1, r2 = func(s, t)
        f.write("{} {}\n".format(r1[:50], r1[-50:]))
        f.write("{} {}\n".format(r2[:50], r2[-50:]))
        f.write("{}\n{}\n{}\n".format(str(cost),
                                      str(round(timeit.default_timer() - start, 3)),
                                      str(tracemalloc.get_traced_memory()[1] // 1024)))


def get_time_and_space(func, s, t):
    """
    Return the time and space used by func
    """
    tracemalloc.start()
    start = timeit.default_timer()
    func(s, t)
    time = timeit.default_timer() - start
    space = tracemalloc.get_traced_memory()[1]
    tracemalloc.clear_traces()
    return round(time, 3), space // 1024


def random_generator():
    """
    Randomly generate a sequence of A, C, T, G of length within 1024
    """
    base = ['A', 'C', 'T', 'G']
    random.shuffle(base)
    return string_generator(''.join(base), [random.randint(1, 4 * 2 ** i) for i in range(random.randint(0, 8))])
