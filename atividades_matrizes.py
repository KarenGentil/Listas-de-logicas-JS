# Programa 1: Leia uma matriz 3x3 e exiba a matriz
matriz = [[int(input(f"Digite o elemento [{i},{j}]: ")) for j in range(3)] for i in range(3)]
print("Matriz:")
for linha in matriz:
    print(linha)

# Programa 2: Leia uma matriz 2x2 e calcule a soma de todos os elementos
matriz = [[int(input(f"Digite o elemento [{i},{j}]: ")) for j in range(2)] for i in range(2)]
soma = sum(sum(linha) for linha in matriz)
print("Soma dos elementos:", soma)

# Programa 3: Leia uma matriz 3x3 e exiba a soma da diagonal principal
matriz = [[int(input(f"Digite o elemento [{i},{j}]: ")) for j in range(3)] for i in range(3)]
diagonal = sum(matriz[i][i] for i in range(3))
print("Soma da diagonal principal:", diagonal)

# Programa 4: Leia duas matrizes 2x2 e exiba a soma delas
matriz1 = [[int(input(f"Digite o elemento da matriz1 [{i},{j}]: ")) for j in range(2)] for i in range(2)]
matriz2 = [[int(input(f"Digite o elemento da matriz2 [{i},{j}]: ")) for j in range(2)] for i in range(2)]
soma_matrizes = [[matriz1[i][j] + matriz2[i][j] for j in range(2)] for i in range(2)]
print("Soma das matrizes:", soma_matrizes)

# Programa 5: Leia uma matriz 3x3 e exiba o maior valor
matriz = [[int(input(f"Digite o elemento [{i},{j}]: ")) for j in range(3)] for i in range(3)]
maior = max(max(linha) for linha in matriz)
print("Maior valor:", maior)

# Programa 6: Leia uma matriz 4x4 e exiba a média dos elementos
matriz = [[int(input(f"Digite o elemento [{i},{j}]: ")) for j in range(4)] for i in range(4)]
todos = [n for linha in matriz for n in linha]
print("Média:", sum(todos)/len(todos))

# Programa 7: Leia duas matrizes 2x2 e exiba o produto entre elas
matriz1 = [[int(input(f"Digite o elemento da matriz1 [{i},{j}]: ")) for j in range(2)] for i in range(2)]
matriz2 = [[int(input(f"Digite o elemento da matriz2 [{i},{j}]: ")) for j in range(2)] for i in range(2)]
produto = [[sum(matriz1[i][k]*matriz2[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
print("Produto das matrizes:", produto)

# Programa 8: Leia uma matriz 3x3 e exiba o menor valor
matriz = [[int(input(f"Digite o elemento [{i},{j}]: ")) for j in range(3)] for i in range(3)]
menor = min(min(linha) for linha in matriz)
print("Menor valor:", menor)

# Programa 9: Leia uma matriz 3x3 e verifique se ela é simétrica
matriz = [[int(input(f"Digite o elemento [{i},{j}]: ")) for j in range(3)] for i in range(3)]
simetrica = all(matriz[i][j] == matriz[j][i] for i in range(3) for j in range(3))
print("É simétrica?", simetrica)

# Programa 10: Leia uma matriz 4x4 e exiba a soma dos elementos de cada coluna
matriz = [[int(input(f"Digite o elemento [{i},{j}]: ")) for j in range(4)] for i in range(4)]
somas_colunas = [sum(matriz[i][j] for i in range(4)) for j in range(4)]
print("Soma por coluna:", somas_colunas)

# Programa 11: Leia duas matrizes 2x2 e verifique se são iguais
matriz1 = [[int(input(f"Digite o elemento da matriz1 [{i},{j}]: ")) for j in range(2)] for i in range(2)]
matriz2 = [[int(input(f"Digite o elemento da matriz2 [{i},{j}]: ")) for j in range(2)] for i in range(2)]
iguais = matriz1 == matriz2
print("São iguais?", iguais)

# Programa 12: Leia uma matriz 3x3 e exiba o produto da diagonal secundária
matriz = [[int(input(f"Digite o elemento [{i},{j}]: ")) for j in range(3)] for i in range(3)]
produto_diag_sec = matriz[0][2]*matriz[1][1]*matriz[2][0]
print("Produto da diagonal secundária:", produto_diag_sec)

# Programa 13: Leia uma matriz 4x4 e exiba o maior valor de cada linha
matriz = [[int(input(f"Digite o elemento [{i},{j}]: ")) for j in range(4)] for i in range(4)]
maiores_linhas = [max(linha) for linha in matriz]
print("Maior valor por linha:", maiores_linhas)

# Programa 14: Leia uma matriz 3x3 e verifique se é identidade
matriz = [[int(input(f"Digite o elemento [{i},{j}]: ")) for j in range(3)] for i in range(3)]
identidade = all(matriz[i][j] == (1 if i == j else 0) for i in range(3) for j in range(3))
print("É identidade?", identidade)

# Programa 15: Leia duas matrizes 2x2 e exiba a subtração entre elas
matriz1 = [[int(input(f"Digite o elemento da matriz1 [{i},{j}]: ")) for j in range(2)] for i in range(2)]
matriz2 = [[int(input(f"Digite o elemento da matriz2 [{i},{j}]: ")) for j in range(2)] for i in range(2)]
subtracao = [[matriz1[i][j] - matriz2[i][j] for j in range(2)] for i in range(2)]
print("Subtração das matrizes:", subtracao)
