import time


def deduction(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def division(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def binary(a, b):
    a, b = b, a if a > b else a
    k = 1
    while a != 0 and b != 0:
        while a % 2 == 0 and b % 2 == 0:
            a //= 2
            b //= 2
            k *= 2
        if a % 2 == 0:
            while a % 2 == 0:
                a //= 2
        elif b % 2 == 0:
            while b % 2 == 0:
                b //= 2
        if a >= b:
            a -= b
        else:
            b -= a
    return b * k


def left_to_right(a, b):
    m = str(bin(b))
    res = 1
    for i in range(2, len(m)):
        if m[i] == '1':
            res = res ** 2 * a
        else:
            res **= 2
    return res


def right_to_left(a, b):
    m = str(bin(b))
    z = a
    res = 1
    for i in range(len(m) - 1, 2, -1):
        if m[i] == '1':
            res *= z
            z **= 2
        else:
            z **= 2
    return res * z


a, b = 12, 9
print(left_to_right(a, b))
print(right_to_left(a, b))
