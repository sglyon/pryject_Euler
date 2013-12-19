from __future__ import division


def triangle(n, ident=False):
    if ident:
        return (3, int(n * (n + 1) / 2))
    else:
        return int(n * (n + 1) / 2)


def square(n, ident=False):
    if ident:
        return (4, int(n ** 2))
    else:
        return int(n ** 2)


def pentagonal(n, ident=False):
    if ident:
        return (5, int(n * (3 * n - 1) / 2))
    else:
        return int(n * (3 * n - 1) / 2)


def hexagonal(n, ident=False):
    if ident:
        return (6, int(n * (2 * n - 1)))
    else:
        return int(n * (2 * n - 1))


def heptagonal(n, ident=False):
    if ident:
        return (7, int(n * (5 * n - 3) / 2))
    else:
        return int(n * (5 * n - 3) / 2)


def octagonal(n, ident=False):
    if ident:
        return (8, int(n * (3 * n - 2)))
    else:
        return int(n * (3 * n - 2))
