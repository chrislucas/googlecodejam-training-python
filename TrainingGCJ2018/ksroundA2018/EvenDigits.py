'''
https://code.google.com/codejam/contest/9234486/dashboard#s=p0
'''

from sys import stdin as _in, stdout as _out


def has_odd_number(n):
    while n >= 1:
        if (n & 1) == 1:
            return True
        n //= 10
    return False


_small = "../raw/ksroundA2018/out/a-small-practice.txt"
_larger = "../raw/ksroundA2018/out/a-larger-practice.txt"


# naive approach
def solver():
    file_writer = open(_larger, "w+")
    cases = int(_in.readline())
    for x in range(1, cases + 1):
        n = int(_in.readline())
        _copy_1 = n
        _copy_2 = n
        if (n & 1) == 1:
            _copy_1 = n + 1
            _copy_2 = n - 1

        while has_odd_number(_copy_1) and has_odd_number(_copy_2):
            _copy_1 += 2
            _copy_2 -= 2

        diff_1 = abs(n - _copy_1)
        diff_2 = abs(n - _copy_2)
        _answer = diff_1 if diff_1 < diff_2 else diff_2
        file_writer.write("Case #%d: %d\n" % (x, _answer))


def solver2():
    _out = open(_larger, "w+")
    cases = int(_in.readline())
    for x in range(1, cases + 1):
        pass

solver()

if __name__ == '__main__':
    pass
