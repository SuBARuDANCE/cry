from sympy import *


def nod():  # Функция нахождения НОД по алгоритму Евглида
    x = int(input("Число 1: "))
    y = int(input("Число 2: "))
    print("НОД: ", x, " и ", y)
    n = 1
    dop = 1
    while dop != 0:
        if x - (int(x / y) * y) == 0:
            break
        dop = x - (int(x / y) * y)
        print("Шаг ", n, ". ", x, " = ", int(x / y), " * ", y, " + ", dop)
        x = y
        y = dop
        n += 1

    print("НОД = ", dop)


def nodv2():  # Функция нахождения НОД по алгоритму Евглида
    print("НОД: ", x := int(input()), " и ", y := int(input()))
    n = 1
    dop = 1
    while dop != 0:
        if x - (int(x / y) * y) == 0:
            break
        dop = x - (int(x / y) * y)
        print("Шаг ", n, ". ", x, " = ", int(x / y), " * ", y, " + ", dop)
        x = y
        y = dop
        n += 1

    print("НОД = ", dop)


def Euler(n):  # Функция Ейлера без решения
    f = n;
    if n % 2 == 0:
        while n % 2 == 0:
            n = n // 2;
        f = f // 2;
    i = 3
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i;
            f = f // i;
            f = f * (i - 1);
        i = i + 2;
    if n > 1:
        f = f // n;
        f = f * (n - 1);
    return f;


def kitOb():  # Функция китайская теорема о  остатках с решением
    print("x =", r1 := int(input("r1 = ")), "mod ", mod1 := int(input("mod = ")))
    #r1 = int(input("r1 = "))
    #mod1 = int(input("mod = "))

    print("x =", r2 := int(input("r2 = ")), "mod ", mod2 := int(input("mod = ")))
    #r2 = int(input("r2 = "))
    #mod2 = int(input("mod = "))

    print("x =", r3 := int(input("r3 = ")), "mod ", mod3 := int(input("mod = ")))
    #r3 = int(input("r3 = "))
    #mod3 = int(input("mod = "))

    M = mod1 * mod2 * mod3
    print("M = ", mod1, "*", mod2, "*", mod3, "=", M)

    M1 = int(M / mod1)
    print("M1 =", M, '/', mod1, "=", M1)

    M2 = int(M / mod2)
    print("M2 =", M, '/', mod2, "=", M2)

    M3 = int(M / mod3)
    print("M3 =", M, '/', mod3, "=", M3)

    print(M1, "* N1 = 1 mod ", mod1)
    mod11 = mod1

    if isprime(mod11):  # Проверка на простое число если нет то расчет по функции Ейлера
        mod11 -= 1
        N1 = int((M1 ** (mod11 - 1)) % mod1)
        print("N1 = ", M1, "^", mod11, "-1 = ", M1, "^", mod11 - 1, " mod ", mod1)
    else:
        mod11 = Euler(mod11)
        N1 = int((M1 ** (mod11 - 1)) % mod1)
        print("N1 = ", M1, "^", mod11, "-1 = ", M1, "^", mod11 - 1, " mod ", mod1)

    print("N1 = ", N1)

    print(M2, "* N2 = 1 mod ", mod2)
    mod21 = mod2

    if isprime(mod21):  # Проверка на простое число если нет то расчет по функции Ейлера
        mod21 -= 1
        N2 = int((M2 ** (mod21 - 1)) % mod2)
        print("N2 = ", M2, "^", mod21, "-1 = ", M2, "^", mod21 - 1, " mod ", mod2)
    else:
        mod21 = Euler(mod21)
        N2 = int((M2 ** (mod21 - 1)) % mod2)
        print("N2 = ", M2, "^", mod21, "-1 = ", M2, "^", mod21 - 1, " mod ", mod2)

    print("N2 = ", N2)

    print(M3, "* N3 = 1 mod ", mod3)
    mod31 = mod3

    if isprime(mod31):  # Проверка на простое число если нет то расчет по функции Ейлера
        mod31 -= 1
        N3 = int((M3 ** (mod31 - 1)) % mod3)
        print("N3 = ", M3, "^", mod31, "-1 = ", M3, "^", mod31 - 1, " mod ", mod3)
    else:
        mod31 = Euler(mod31)
        N3 = int((M3 ** (mod31 - 1)) % mod3)
        print("N3 = ", M3, "^", mod31, "-1 = ", M3, "^", mod31 - 1, " mod ", mod3)
    print("N3 = ", N3)

    x1 = int(M1 * N1)
    print("x1 = ", M1, "*", N1, " = ", x1)

    x2 = int(M2 * N2)
    print("x2 = ", M2, "*", N2, " = ", x2)

    x3 = int(M3 * N3)
    print("x3 = ", M3, "*", N3, " = ", x3)

    x = int((x1 * r1 + x2 * r2 + x3 * r3) % M)  # расчет Х ответ в китайской функции
    print("x =", x1, "*", r1, "+", x2, "*", r2, "+", x3, "*", r3, " = ", x1 * r1 + x2 * r2 + x3 * r3, " mod ", M, " = ",
          x)

    print("Проверка :")  # Проверка для записи (не нужна функции)
    print(x, "= ", x % mod1, " mod ", mod1)
    # if x%mod1 == r1:
    #    print(True)
    # else:
    #    print(False)

    print(x, "= ", x % mod2, " mod ", mod2)
    # if x%mod2 == r2:
    #    print(True)
    # else:
    #    print(False)

    print(x, "= ", x % mod3, " mod ", mod3)
    # if x%mod3 == r3:
    #    print(True)
    # else:
    #    print(False)


kitOb()
