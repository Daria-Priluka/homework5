A = int(input("Введите число, которое хотите перевести в другую систему счисления: "))

B = int(input("В какую систему счисления Вы хотите перевести число: 2 или 8?: "))
if B == 2 or B == 8:
    while A>0:
    S= str(A%B) + S
    A //= B
print(S)
