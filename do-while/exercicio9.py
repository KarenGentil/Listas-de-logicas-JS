# Nome e idade de 5 pessoas usando do-while
contador = 0
soma_idades = 0
while True:
    nome = input(f"Digite o nome da pessoa {contador+1}: ")
    idade = int(input("Digite a idade: "))
    soma_idades += idade
    contador += 1
    if contador == 5:
        break
print("Média das idades:", soma_idades/5)
