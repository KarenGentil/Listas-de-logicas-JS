# Primeiros 20 números da Fibonacci usando do-while
a, b = 0, 1
contador = 0
while True:
    if contador == 20:
        break
    print(a)
    a, b = b, a + b
    contador += 1
