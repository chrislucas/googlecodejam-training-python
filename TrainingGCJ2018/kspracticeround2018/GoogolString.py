'''
https://code.google.com/codejam/contest/4374486/dashboard#s=p1
'''

_small = "../raw/kspr2018/out/b-small-practice.txt"
_larger = "../raw/kspr2018/out/b-larger-practice.txt"

'''
Tamanho da string no final do metodo naive_test = 2 ^ (n - 1) - 1
'''


def naive_test(n):
    i = 1
    _str_i, _str_j = "", ""
    while i <= n:
        # tornar a string si+1 em si para realizar a concatenacao mais tarde
        _str_j = _str_i
        # reverse
        _str_i = _str_i[::-1]
        # switch
        si = "".join(["0" if _str_i[j] == "1" else "1" for j in range(0, len(_str_i))])
        # si+1 = si + 0 + swich(reverse(si))
        _str_j += "0" + si
        _str_i = _str_j
        i += 1
    return _str_i


def test():
    for x in range(1, 10):
        _str = naive_test(x)
        l = len(_str) - 7
        r = len(_str)
        print("%d %s ... %d" % (x, _str, len(_str)))


'''
A string Googol segue um padrao. sempre o (2^i)-esimo caracter eh '0'
entao se k for uma potencia de 2 a funcao retorna '0' imediatamente
@solver
'''
def solver(k):
    '''
    from math import log, floor
    nearest_2_power = floor(log(k, 2))
    if k == 2 ** nearest_2_power:
        return '0'
    '''

    # teste se k eh uma potencia de 2 mais eficiente do que o acima
    if (k & (k - 1)) == 0:
        return '0'

    return '1'


print(solver(32))

if __name__ == '__main__':
    pass
