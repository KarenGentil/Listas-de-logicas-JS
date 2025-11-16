# Fibonacci até um número usando do-while
limite = int(input("Digite um número: "))
a, b = 0, 1
while True:
    if a > limite:
        break
    print(a)
    a, b = b, a + b
