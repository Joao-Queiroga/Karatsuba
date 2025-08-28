def dividir_numero(n: int, m: int):
    s = str(n)
    if len(s) <= m:
        return 0, m
    return int(s[:-m]), int(s[-m:])


def karatsuba(x: int, y: int):
    if abs(x) < 10 or abs(y) < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    a, b = dividir_numero(x, m)
    c, d = dividir_numero(y, m)

    p1 = karatsuba(a, c)
    p2 = karatsuba(b, d)
    p3 = karatsuba(a + b, c + d)

    m = max(len(str(x)), len(str(y))) // 2

    return p1 * 10 ** (2 * m) + (p3 - p1 - p2) * 10**m + p2


x = int(input("Digite o primeiro fator da multiplicação: "))
y = int(input("Digite o segundo fator da multiplicação: "))

print("%d * %d = %d" % (x, y, karatsuba(x, y)))
