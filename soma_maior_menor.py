soma = 0
numeros = 1
resposta = 's'


while resposta == 's':
    n = int(input('digite um numero: '))
    if numeros == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma+= n
    resposta = input('deseja continuar digitando? s/n: ')
    while resposta != 's' and resposta !='n':
        resposta = input('deseja continuar digitando?? s/n: ')
    if resposta == 's':
        numeros += 1
print('quantidade de numeros somados {}'.format(numeros))
print(f'soma = {soma}')
print(f'menor número digitado {menor}')
print(f'maior número digitado {maior}')