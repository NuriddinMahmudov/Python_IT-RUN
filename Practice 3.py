# def boolean29(x,y,x1,y1,x2,y2):
#     if x1<x<x2 and y1>y>y2:
#         return True
#     else:
#         return False
#
# print((boolean29(5,5,3,7,8,2)))


# def if4(a,b,c):
#     if a>=0 or b>=0 or c>=0:
#         return True
#     else:
#         return False
#
# print(if4(2,4,7))


# def if8(a,b):
#     if a > b:
#         print(a)
#         print(b)
#     else:
#         print(b)
#         print(a)
#
# if8(4,67)


# def if9(A,B):
#     if A > B:
#         A,B = B,A
#         print("A =", A, "B =", B)
#     else:
#         print("A =", A, "B =", B)
#
# if9(8,4)


# def if12(a,b,c):
#     if a>c and b>c:
#         print(c)
#     elif a>b and c>b:
#         print(b)
#     elif b>a and c>a:
#         print(a)
#
# if12(5,6,3)


# def for1(k,n):
#     for i in range(n):
#         print(k)
#
# for1(4,7)


# def for2(a,b):
#     for i in range(a,b+1):
#         print(i)
#     n = b-a+1
#     print("N =", n)
#
# for2(3,12)


# def for3(a,b):
#     for i in range(b-1,a,-1):
#         print(i)
#     n = b-a-1
#     print("N =", n)
#
# for3(3,14)


# def for4(n):
#     for i in range(1,11):
#         k = i * n
#         print(i,"кг конфет стоит",k)
#
# for4(5)


# def for5(n):
#     v = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
#     for i in v:
#         k = i * n
#         print(i,"кг конфет стоит",round(k,2))
#
# for5(17)


# def for6(n):
#     v = [1.2,1.4,1.6,1.8,2]
#     for i in v:
#         k = i * n
#         print(i,"кг конфет стоит",round(k,2))
#
# for6(22)


# def for7(a,b):
#     n = 0
#     for i in range(a,b+1):
#         n += i
#     print(n)
#
# for7(2,8)


# def for8(a,b):
#     n = 1
#     for i in range(a,b+1):
#         n *= i
#     print(n)
#
# for8(4,10)


# def for9(a,b):
#     n = 0
#     for i in range(a,b+1):
#         i **= 2
#         n += i
#     print(n)
#
# for9(2,5)


# def for10(n):
#     k = 0
#     for i in range(1,n+1):
#         k += 1/i
#     print(round(k,3))
#
# for10(7)