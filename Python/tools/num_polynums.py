from numba import autojit


@autojit
def triangle(n):
    return n * (n + 1) / 2


@autojit
def square(n):
    return n ** 2


@autojit
def pentagonal(n):
    return n * (3 * n - 1) / 2


@autojit
def hexagonal(n):
    return n * (2 * n - 1)


@autojit
def heptagonal2(n):
    return n * (5 * n - 3) / 2


@autojit
def octagonal(n):
    return n * (3 * n - 2)
