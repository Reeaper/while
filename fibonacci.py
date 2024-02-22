quantia = int(input('Quantos termos fibonacci você deseja? '))
anterior = 0
atual = 1
contador = 1

while contador <= quantia:
    print('{} -'.format(atual),end=" ")
    proximo = anterior + atual
    anterior = atual
    atual = proximo
    contador += 1
    print(contador)
print('Fim do programa Fibonacci')