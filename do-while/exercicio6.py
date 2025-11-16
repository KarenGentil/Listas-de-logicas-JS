# Divisores de um número usando do-while
num = int(input("Digite um número positivo: "))
divisor = 1
while True:
    if num % divisor == 0:
        print(divisor)
    divisor += 1
    if divisor > num:
        break
