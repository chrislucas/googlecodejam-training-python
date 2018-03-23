'''
https://code.google.com/codejam/contest/4374486/dashboard
'''

from sys import stdin as _in, stdout as _out

_small = "../raw/kspr2018/out/a-small-practice.txt"
_larger = "../raw/kspr2018/out/a-larger-practice.txt"


def read_int():
    return int(_in.readline())


def read_line():
    return _in.readline()


def read_ints():
    return [int(x) for x in read_line().split(" ")]


def read_pair_ints(n):
    _line = read_line().split(" ")
    _ints = [None] * n
    for idx in range(0, n):
        _ints[idx] = [int(_line[idx * 2]), int(_line[idx * 2 + 1])]
    return _ints


def run():
    file_writer = open(_larger, "w+")
    cases = read_int()
    for x in range(1, cases + 1):
        n = read_int()
        g_buzz = read_pair_ints(n)
        q_cities = read_int()
        acc = [0] * q_cities
        for y in range(0, q_cities):
            city = read_int()
            for k in range(0, len(g_buzz)):
                pair = g_buzz[k]
                if pair[0] <= city <= pair[1]:
                    acc[y] += 1
        msg = ' '.join(str(x) for x in acc)
        file_writer.write("Case #%d: %s\n" % (x, msg))
        if x < cases:
            read_line()


run()

if __name__ == '__main__':
    pass
