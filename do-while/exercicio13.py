# Dígitos separados usando do-while
num = int(input("Digite um número: "))
while True:
    digito = num % 10
    print(digito)
    num //= 10
    if num == 0:
        break
