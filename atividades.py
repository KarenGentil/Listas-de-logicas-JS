# Programa 1: Leia 5 números inteiros e exiba-os na ordem inversa
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
print("Ordem inversa:", nums[::-1])

# Programa 2: Leia 10 números inteiros e exiba a soma deles
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]
print("Soma:", sum(nums))

# Programa 3: Leia 7 números inteiros e exiba a média aritmética
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(7)]
print("Média:", sum(nums)/len(nums))

# Programa 4: Leia 5 números inteiros e exiba quantos são pares
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
pares = sum(1 for n in nums if n % 2 == 0)
print("Quantidade de pares:", pares)

# Programa 5: Leia 5 números inteiros e exiba o maior e o menor valor
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
print("Maior:", max(nums), "Menor:", min(nums))

# Programa 6: Leia 10 números inteiros e exiba-os em ordem crescente
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]
print("Ordem crescente:", sorted(nums))

# Programa 7: Leia 10 números inteiros e exiba quantos são positivos
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]
positivos = sum(1 for n in nums if n > 0)
print("Quantidade de positivos:", positivos)

# Programa 8: Leia 5 números inteiros e calcule a média dos pares e ímpares
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
pares = [n for n in nums if n % 2 == 0]
impares = [n for n in nums if n % 2 != 0]
print("Média pares:", sum(pares)/len(pares) if pares else 0)
print("Média ímpares:", sum(impares)/len(impares) if impares else 0)

# Programa 9: Leia 10 números inteiros e exiba quantidade de positivos e negativos
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]
positivos = sum(1 for n in nums if n > 0)
negativos = sum(1 for n in nums if n < 0)
print("Positivos:", positivos, "Negativos:", negativos)

# Programa 10: Leia 5 números inteiros e verifique se algum é zero
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
print("Existe zero?", any(n == 0 for n in nums))

# Programa 11: Leia 10 números inteiros e exiba soma dos positivos e soma dos negativos
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]
positivos = sum(n for n in nums if n > 0)
negativos = sum(n for n in nums if n < 0)
print("Soma positivos:", positivos, "Soma negativos:", negativos)

# Programa 12: Leia 5 números inteiros e exiba-os em ordem decrescente
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(5)]
print("Ordem decrescente:", sorted(nums, reverse=True))

# Programa 13: Leia 10 números inteiros e exiba quantos estão no intervalo de 10 a 50
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]
intervalo = sum(1 for n in nums if 10 <= n <= 50)
print("Quantidade no intervalo [10,50]:", intervalo)

# Programa 14: Leia 7 números inteiros e exiba apenas os pares
nums = [int(input(f"Digite o {i+1}º número: ")) for i in range(7)]
pares = [n for n in nums if n % 2 == 0]
print("Números pares:", pares)

# Programa 15: Leia 5 nomes e exiba-os em ordem alfabética
nomes = [input(f"Digite o {i+1}º nome: ") for i in range(5)]
print("Ordem alfabética:", sorted(nomes))
