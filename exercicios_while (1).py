# Exercícios com loop WHILE
# Autor: Gerado automaticamente
# Linguagem: Python 3

# =============================
# 1) Exibir números de 1 a 10
# =============================
i = 1
while i <= 10:
    print(i)
    i += 1

# =============================
# 2) Soma dos números de 1 a 100
# =============================
i = 1
soma = 0
while i <= 100:
    soma += i
    i += 1
print("Soma de 1 a 100:", soma)

# =============================
# 3) Números pares de 1 a 50
# =============================
i = 2
while i <= 50:
    print(i)
    i += 2

# =============================
# 4) Ler 5 números e calcular média
# =============================
i = 1
soma = 0
while i <= 5:
    num = int(input(f"Digite o {i}º número: "))
    soma += num
    i += 1
media = soma / 5
print("Média:", media)

# =============================
# 5) Tabuada de um número
# =============================
num = int(input("Digite um número para a tabuada: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# =============================
# 6) Divisores de um número
# =============================
num = int(input("Digite um número positivo: "))
i = 1
while i <= num:
    if num % i == 0:
        print(i)
    i += 1

# =============================
# 7) Verificar se é primo
# =============================
num = int(input("Digite um número: "))
i = 2
eh_primo = True
while i < num:
    if num % i == 0:
        eh_primo = False
        break
    i += 1
if eh_primo and num > 1:
    print("É primo")
else:
    print("Não é primo")

# =============================
# 8) Fibonacci até um número
# =============================
limite = int(input("Digite um número para Fibonacci: "))
a, b = 0, 1
while a <= limite:
    print(a)
    a, b = b, a + b

# =============================
# 9) Nome e idade de 5 pessoas
# =============================
i = 1
soma_idades = 0
while i <= 5:
    nome = input(f"Digite o nome da pessoa {i}: ")
    idade = int(input("Digite a idade: "))
    soma_idades += idade
    i += 1
media = soma_idades / 5
print("Média das idades:", media)

# =============================
# 10) Primeiros 20 números da Fibonacci
# =============================
a, b = 0, 1
i = 1
while i <= 20:
    print(a)
    a, b = b, a + b
    i += 1

# =============================
# 11) Soma dos pares até um número
# =============================
num = int(input("Digite um número: "))
i = 2
soma = 0
while i <= num:
    soma += i
    i += 2
print("Soma dos pares:", soma)

# =============================
# 12) Números ímpares de 1 a 50
# =============================
i = 1
while i <= 50:
    print(i)
    i += 2

# =============================
# 13) Dígitos separados
# =============================
num = int(input("Digite um número: "))
while num > 0:
    digito = num % 10
    print(digito)
    num //= 10

# =============================
# 14) Fatorial de um número
# =============================
num = int(input("Digite um número para fatorial: "))
fatorial = 1
while num > 0:
    fatorial *= num
    num -= 1
print("Fatorial:", fatorial)

# =============================
# 15) Ler nome e idade até "fim"
# =============================
soma_idades = 0
contador = 0
while True:
    nome = input("Digite o nome (ou 'fim' para encerrar): ")
    if nome.lower() == "fim":
        break
    idade = int(input("Digite a idade: "))
    soma_idades += idade
    contador += 1
if contador > 0:
    print("Média das idades:", soma_idades / contador)
else:
    print("Nenhuma idade informada.")
