import random

opcao = int(input('Para gerar uma senha automatica, digite 1, caso deseje cadastrar uma senha digite 2\n'))

if opcao == 1:
    senha = str(random.randint (1000,9999))
    print('A sua senha é', senha)
else:
    senha = input('Digite uma senha com quatro numeros:\n')
    tamanho_senha = len(senha)

if len(senha) != 4:
    print('A senha deve conter 4 numeros, tente novamente do inicio')

acesso = input('Digite sua Senha:\n')
if acesso == senha:
    print('Acesso liberado')
else:
    print('Acesso negado')