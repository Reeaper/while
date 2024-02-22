soma = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você somou {cont} números')
print(f'A soma de todos foi {soma}')