# Fatorial usando do-while
num = int(input("Digite um número: "))
fatorial = 1
while True:
    fatorial *= num
    num -= 1
    if num == 0:
        break
print("Fatorial:", fatorial)
