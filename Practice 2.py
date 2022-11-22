# def integer1(L):
#     m = L // 100
#     print(L, "сантиметров =", m, "метров")
#
# integer1(256)


# def integer2(M):
#     T = M // 1000
#     print(M, "килограмм =", T, "тонн")
#
# integer2(4632)


# def integer3(bites):
#     kbites = bites // 1024
#     print(bites, "=", kbites)
#
# integer3(456456)


# def integer11(n):
#     s = str(n)
#     print(int(s[0])+int(s[1])+int(s[2]))
#     print(int(s[0]) * int(s[1]) * int(s[2]))
#
# integer11(575)


# def integer20(N):
#     H = N // 3600
#     print(N, "секунд =", H, "часов")
#
# integer20(34638)


# def integer24(K):
#     w = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]
#     y = K % 7
#     print(w[y], y)
#
# integer24(55)


# def integer29(A, B, C):
#     sp = A*B
#     sk = C**2
#     kolvo = sp // sk
#     s = sp - (sk * kolvo)
#     print("Площадь прямоугольника со сторонами A и B:", sp)
#     print("Площадь квадрата со стороной C:", sk)
#     print("Количество целых квадратов в прямоугольнике:", kolvo)
#     print("Площадь не занятой части прямоугольника:", s)
#
# integer29(5,8,3)


# def integer30(y):
#     if y % 10 == 0 and (y // 10) % 10 == 0:
#         v = (y // 100)
#     else:
#         v = (y // 100) + 1
#     print(y, "год =", v, "столетие")
#
# integer30(2040)

# def boolean1(A):
#     if A >= 0:
#         return True
#     else:
#         return False
#
# print(boolean1(34))


# def boolean2(A):
#     if A % 2 == 1:
#         return True
#     else:
#         return False
#
# print(boolean2(7))


# def boolean3(A):
#     if A % 2 == 0:
#         return True
#     else:
#         return False
#
# print(boolean3(8))


# def boolean4(A,B):
#     if A>2 and B <= 3:
#         return True
#     else:
#         return False
#
# print(boolean4(4,3))


# def boolean5(A,B):
#     if A>=0 or B<-2:
#         return True
#     else:
#         return False
#
# print(boolean5(0,-2))


# def boolean6(A,B,C):
#     if A<B<C:
#         return True
#     else:
#         return False
#
# print(boolean6(2,4,6))


# def boolean7(A,B,C):
#     if A>B>C or A<B<C:
#         return True
#     else:
#         return False
#
# print(boolean7(4,6,8))


# def boolean8(A,B):
#     if A % 2 == 1 and B % 2 ==1:
#         return True
#     else:
#         return False
#
# print(boolean8(3,5))


# def boolean9(A,B):
#     if A % 2 == 1 or B % 2 ==1:
#         return True
#     else:
#         return False
#
# print(boolean9(4,9))


# def boolean10(A,B):
#     if A % 2 == 1 and B % 2 == 0 or A % 2 == 0 and B % 2 == 1:
#         return True
#     else:
#         return False
#
# print(boolean10(4,5))


# def boolean11(A,B):
#     if A%2==0 and B%2==0 or A%2==1 and B%2==1:
#         return True
#     else:
#         return False
#
# print(boolean11(7,3))


# def boolean12(A,B,C):
#     if A>=0 and B>=0 and C>=0:
#         return True
#     else:
#         return False
#
# print(boolean12(5,7,3))


# def boolean13(A,B,C):
#     if A>=0 or B>=0 or C>=0:
#         return True
#     else:
#         return False
#
# print(boolean13(0,-9,3))


# def boolean14(A,B,C):
#     if A>=0 and B<0 and C<0 or A<0 and B>=0 and C<0 or A<0 and B<0 and C>=0:
#         return True
#     else:
#         return False
#
# print(boolean14(-6,-1,5))


# def boolean15(A,B,C):
#     if A >= 0 and B >= 0 and C < 0 or A < 0 and B >= 0 and C >= 0 or A >= 0 and B < 0 and C >= 0:
#         return True
#     else:
#         return False
#
# print(boolean15(-6,8,5))