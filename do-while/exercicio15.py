# Ler nome e idade até 'fim' usando do-while
soma_idades = 0
contador = 0
while True:
    nome = input("Digite o nome (ou 'fim' para encerrar): ")
    if nome.lower() == 'fim':
        break
    idade = int(input("Digite a idade: "))
    soma_idades += idade
    contador += 1
if contador > 0:
    print("Média das idades:", soma_idades/contador)
else:
    print("Nenhuma idade informada.")
