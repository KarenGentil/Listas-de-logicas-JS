# Soma dos pares até um número usando do-while
num = int(input("Digite um número: "))
i = 2
soma = 0
while True:
    soma += i
    i += 2
    if i > num:
        break
print("Soma dos pares:", soma)
