from sequence_alignment_efficient import sequence_alignment_efficient
from sequence_alignment_basic import sequence_alignment_basic
from utility import random_generator, get_time_and_space
import matplotlib.pyplot as plt


def plot(n):
    """
    Plot graph of
        a) problem size n vs memory used
        b) problem size n vs cpu time
    """
    time_base, space_base, time_efficient, space_efficient, problem_size = [], [], [], [], []
    ss, ts = sorted([random_generator() for _ in range(n)], key=lambda x: len(x)), \
             sorted([random_generator() for _ in range(n)], key=lambda x: len(x))
    for i in range(n):
        s, t = ss[i], ts[i]
        problem_size.append(len(s) + len(t))
        t_base, s_base = get_time_and_space(sequence_alignment_basic, s, t)
        t_eff, s_eff = get_time_and_space(sequence_alignment_efficient, s, t)
        time_base.append(t_base)
        space_base.append(s_base)
        time_efficient.append(t_eff)
        space_efficient.append(s_eff)

    plt.plot(problem_size, time_base, label="base")
    plt.plot(problem_size, time_efficient, label="efficient")
    plt.xlabel('problem size')
    plt.ylabel('seconds')
    plt.title('CPU Plot')
    plt.legend()
    plt.savefig("CPUPlot.png")
    plt.show()

    plt.plot(problem_size, space_base, label="base")
    plt.plot(problem_size, space_efficient, label="efficient")
    plt.xlabel('problem size')
    plt.ylabel('kib')
    plt.title('Memory Plot')
    plt.legend()
    plt.savefig("MemoryPlot.png")
    plt.show()


if __name__ == '__main__':
    plot(15)
