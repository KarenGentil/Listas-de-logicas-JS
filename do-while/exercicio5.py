# Tabuada de um número usando do-while
num = int(input("Digite um número: "))
contador = 1
while True:
    print(f"{num} x {contador} = {num*contador}")
    contador += 1
    if contador > 10:
        break
