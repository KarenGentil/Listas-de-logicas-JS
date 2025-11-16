# Ler 5 números e calcular média usando do-while
contador = 0
soma = 0
while True:
    num = int(input(f"Digite o {contador+1}º número: "))
    soma += num
    contador += 1
    if contador == 5:
        break
print("Média:", soma/5)
