from random import randint
from math import gcd


def deduction_gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def division_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def binary_gcd(a, b):
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
    m = bin(b)
    res = 1
    for i in range(2, len(m)):
        if m[i] == '1':
            res = res ** 2 * a
        else:
            res **= 2
    return res


def right_to_left(a, b):
    m = bin(b)
    z = a
    res = 1
    for i in range(len(m) - 1, 2, -1):
        if m[i] == '1':
            res *= z
            z **= 2
        else:
            z **= 2
    return res * z


def is_prime_ferma(n, count=1):
    for i in range(count):
        a = randint(1, n - 1)
        if binary_gcd(a, n) == 1:
            if left_to_right(a, n - 1) % n != 1:
                return False
        else:
            return False
    return True


def legandre(a, p):
    if a == 1:
        return 1
    if a % 2 == 0:
        return legandre(a // 2, p) * (-1) ** ((p ** 2 - 1) // 8)
    elif a % 2 != 0 and a != 1:
        return legandre(p % a, a) * (-1) ** (((a - 1) * (p - 1)) // 4)


def yakobi(a, b):
    if binary_gcd(a, b) != 1:
        return 0
    r = 1
    if a < 0:
        a *= -1
        if b % 4 == 3:
            r *= -1
    t = 0
    while a != 0:
        while a % 2 != 0:
            t += 1
            a //= 2
        if t % 2 == 1:
            if b % 8 == 3 or b % 8 == 5:
                r *= -1
        a, b = b % a, a
    else:
        return r


# тесты
if __name__ == "__main__":
    x, y = 219, 383
    if deduction_gcd(x, y) == division_gcd(x, y) == binary_gcd(x, y) == gcd(x, y):
        print("Верно")
    else:
        print("Не верно")
    if left_to_right(x, y) == right_to_left(x, y) == x ** y:
        print("Верно")
    else:
        print("Не верно")
    print(yakobi(x, y))
    print(legandre(x, y))
