# importaçao de biblioteca
import random
# ptuser = pontos do user ptcpu= pontos do computador
ptuser = ptcpu = 0
while True:
    n = int(input('Escolha um número de 0 a 10:'))
    parouimpar = input('par ou impar? p/i ')
    while parouimpar != 'p' and parouimpar != 'i':
        parouimpar= input("Resposta inválida")
    cpu = random.randint(0,10)
    print(f'Valor da CPU {cpu}')
    soma = n + cpu
    if soma %2 == 0 and parouimpar == 'p':
        ptuser +=1
    elif soma %2 == 1 and parouimpar =='i':
        ptuser +=1
    else:
        ptcpu += ptcpu
        break
print(f'Você ganhou {ptuser} partidas')