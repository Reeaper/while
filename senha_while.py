senha ="12345"
leitura =" "
while(leitura != senha):
    leitura = input('Digite a senha numerica: ')
    if leitura == senha:
        print('Acesso liberado')
    else:
        print('Senha incorreta')