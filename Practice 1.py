# def begin1(a):
#     p = 4 * a
#     print("p =", p)
#
# begin1(4)


# def begin2(a):
#     s = a ** 2
#     print("s =", s)
#
# begin2(5)


# def begin3(a, b):
#     s = a * b
#     p = 2*(a+b)
#     print("s =", s)
#     print("p =", p)
#
# begin3(3, 5)


# def begin4(d):
#     L = 3.14 * d
#     print("L =", L)
#
# begin4(7)


# def begin5(a):
#     V = a ** 3
#     S = 6 * (a ** 2)
#     print("V =", V)
#     print("S =", S)
#
# begin5(9)


# def begin6(a, b, c):
#     V = a*b*c
#     S = 2*(a*b + b*c + a*c)
#     print(V)
#     print(S)
#
# begin6(1, 2, 3)


# def begin7(R):
#     L = 2 * 3.14 * R
#     S = 3.14 * (R**2)
#     print("L =", L)
#     print("S =", S)
#
# begin7(9)


# def begin8(a, b):
#     sred = (a + b) / 2
#     print("среднее арифметическое значение", sred)
#
# begin8(2, 4)


# def begin9(a, b):
#     sred = (a * b) ** (1/2)
#     print("среднее геометрическое значение", sred)
#
# begin9(2, 4)


# def begin10(a, b):
#     a = a**2
#     b = b**2
#     sum = a + b
#     raznost = a / b
#     proizvedenie = a * b
#     chastnoe = (a ** 2)/(b ** 2)
#     print("сумма", sum)
#     print("разность", raznost)
#     print("произведение", proizvedenie)
#     print("частное", chastnoe)
#
# begin10(6, 2)


# def begin11(a, b):
#     a = abs(a)
#     b = abs(b)
#     sum = (a + b)
#     raznost = (a / b)
#     proizvedenie = a * b
#     chastnoe = (a ** 2)/(b ** 2)
#     print("сумма", sum)
#     print("разность", raznost)
#     print("произведение", proizvedenie)
#     print("частное", chastnoe)
#
# begin11(8, -2)


# def begin12(a, b, c):
#     C = ((a**2)+(b**2))/0.5
#     P = a+b+c
#     print("C =", C)
#     print("P =", P)
#
# begin12(3, 7, 9)


# def begin13(R1, R2):
#     S1 = 3.14 * (R1**2)
#     S2 = 3.14 * (R2**2)
#     S3 = S1-S2
#     print("S1 =", S1)
#     print("S2 =", S2)
#     print("S3 =", S3)
#
# begin13(7, 6)


# def begin14(L):
#     R = L/(2 * 3.14)
#     S = 3.14 * (R**2)
#     print("R =", R)
#     print("S =", S)
#
# begin14(20)


# def begin15(S):
#     D = ((4 * S) / 3.14) ** 0.5
#     L = 3.14 * D
#     print("D =", D)
#     print("L =", L)
#
# begin15(15)


# def begin18(A, B, C):
#     if A < C < B:
#         proizvedenie = (C - A) * (B - C)
#     else:
#         return None
#     print("произведение длин отрезков AC и BC =", proizvedenie)
#
# begin18(2, 8, 6)


# def begin33(X, Y):
#     A = 10
#     kg = A / X
#     Y = kg * Y
#     print("1 кг конфет стоит", kg)
#     print("Y кг конфет стоит", Y)
#
# begin33(1, 5)


# def begin34(x, a, y, b):
#     konfet_kg = a / x
#     iris_kg = b / y
#     raznost = konfet_kg / iris_kg
#     print("1 кг конфет стоит", round(konfet_kg,2))
#     print("1 кг ирисок стоит", round(iris_kg,2))
#     print("конфеты дороже ирисок в", round(raznost,2), "раза")
#
# begin34(2, 10, 3, 5)


# def begin35(V, T1, U, T2):
#     S1 = V * T1
#     S2 = (V-U) * T2
#     print("Пройденный путь по озеру", S1)
#     print("Пройденный путь по реке", S2)
#
# begin35(5, 2, 3, 2)


# def begin36(V1, V2, S, T):
#     S_obshee = T * (V1 + V2)
#     S_cherez_T = S + S_obshee
#     print("Расстояние между машинами через", T, "часов", S_cherez_T, "метров")
#
# begin36(10, 15, 10, 4)