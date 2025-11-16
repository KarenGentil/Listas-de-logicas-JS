# Verificar se é primo usando do-while
num = int(input("Digite um número: "))
i = 2
primo = True
while True:
    if i >= num:
        break
    if num % i == 0:
        primo = False
        break
    i += 1
if primo and num > 1:
    print("É primo")
else:
    print("Não é primo")
