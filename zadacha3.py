from random import randint
from math import gcd


# Лаба 1
def evclid_gcd(a, b):
    r = [a, b]
    i = 1
    r.append(r[i - 1] % r[i])
    while r[i + 1] != 0:
        i += 1
        r.append(r[i - 1] % r[i])
    else:
        return r[i]


def extended_evclid_gcd(a, b):
    r = [a, b]
    x = [1, 0]
    y = [0, 1]
    i = 1
    while r[i] != 0:
        q = r[i - 1] // r[i]
        r[i - 1], r[i] = r[i], r[i - 1] - q * r[i]
        x[i - 1], x[i] = x[i], x[i - 1] - q * x[i]
        y[i - 1], y[i] = y[i], y[i - 1] - q * y[i]
    return {"коэфы Безу": (x[i - 1], y[i - 1]),
            "НОД": r[i - 1],
            "Частные от деления на НОД": (y[i], x[i])}


def binary_evclid_gcd(a, b):
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


def extended_binary_evclid_gcd(a, b):
    g = 1
    while a % 2 == b % 2 == 0:
        a //= 2
        b //= 2
        g *= 2
    u = a
    v = b
    A = 1
    B = 0
    C = 0
    D = 0
    while u != 0:
        while u % 2 == 0:
            u //= 2
            if A % 2 == B % 2 == 0:
                A //= 2
                B //= 2
            else:
                A = (A + b) // 2
                B = (B - a) // 2
        while v % 2 == 0:
            v //= 2
            if C % 2 == D % 2 == 0:
                C //= 2
                D //= 2
            else:
                C = (C + b) // 2
                D = (D - a) // 2
        if u >= v:
            u -= v
            A -= C
            B -= D
        else:
            v -= u
            C -= A
            D -= b
    return {"НОД": g * v, "x": C, "y": D}


def any_numbers_gcd(func, *digits):
    digits = list(digits)
    for i in range(len(digits) - 1):
        digits[i + 1] = func(digits[i], digits[i + 1])
    return digits[-1]


# Лаба 2
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


# Лаба 4
def is_prime_ferma(n):
    a = randint(1, n - 1)
    if binary_evclid_gcd(a, n) == 1:
        if left_to_right(a, n - 1) % n != 1:
            return False
    else:
        return False
    return True


def is_prime_solovei_shtrassen(n):
    a = randint(2, n)
    if binary_evclid_gcd(a, n) > 1:
        return False
    j = left_to_right(a, (n - 1) // 2) % n
    jacob_sym = yakobi(a, n)
    if j != jacob_sym:
        return False
    return True

# Лаба 3
def legandre(a, p):
    if a == 1:
        return 1
    if a % 2 == 0:
        return legandre(a // 2, p) * (-1) ** ((p ** 2 - 1) // 8)
    elif a % 2 != 0 and a != 1:
        return legandre(p % a, a) * (-1) ** (((a - 1) * (p - 1)) // 4)


def yakobi(a, b):
    if binary_evclid_gcd(a, b) != 1:
        return 0
    r = 1
    if a < 0:
        a *= -1
        if b % 4 == 3:
            r *= -1
    t = 0
    while a != 0:
        while a % 2 == 0:
            t += 1
            a //= 2
        if t % 2 == 1:
            if b % 8 == 3 or b % 8 == 5:
                r *= -1
        if a % 4 == 3 and b % 4 == 3:
            r *= -1
        a, b = b % a, a
    else:
        return r


# тесты
if __name__ == "__main__":
    x, y = 12, 145
    if evclid_gcd(x, y) == extended_evclid_gcd(x, y)["НОД"] == \
            binary_evclid_gcd(x, y) == extended_binary_evclid_gcd(x, y)["НОД"] == gcd(x, y):
        print("-" * 50)
        print("Евклиды: Верно")
        print(extended_evclid_gcd(x, y))
        print(extended_binary_evclid_gcd(x, y))
        print(any_numbers_gcd(evclid_gcd, 64, 32, 16, 12, 8, 4))
        print("-" * 50)
    else:
        print("-" * 50)
        print("Евклиды: Не верно")
        print("Алгоритм Евклида: ", evclid_gcd(x, y), '\n',
              "Расширенный алгоритм: ", extended_evclid_gcd(x, y)["НОД"], '\n',
              "Бинарный алгоритм: ", binary_evclid_gcd(x, y), '\n',
              "Расширенный бинарный: ", extended_binary_evclid_gcd(x, y)["НОД"], '\n',
              "Питоновский: ", gcd(x, y))
        print("-" * 50)
    if left_to_right(x, y) == right_to_left(x, y) == x ** y:
        print("Степени: Верно")
        print("-" * 50)
    else:
        print("Степени: Не верно")
        print("Слева направо: ", left_to_right(x, y), "\n",
              "Справа налево: ", right_to_left(x, y), "\n",
              "Обычное: ", x ** y)
        print("-" * 50)
    print("Символ Якоби: ", yakobi(x, y))
    print("-" * 50)
    print("Символ Лежандра :", legandre(x, y))
    print("-" * 50)
    print(any_numbers_gcd(evclid_gcd, x, y))
    print(is_prime_ferma(x))
    print(is_prime_solovei_shtrassen(x))
