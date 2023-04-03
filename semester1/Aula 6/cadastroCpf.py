cadastro = []

n = input('cpf: ')

if n in cadastro:

    k = input('chave atualizar: ')

    if k in cadastro[n]:
        atualizar = input('valor atualizar: ')
        cadastro[n][k] = atualizar
    
    else:
        print('chave informada não encontrada')

else:
    print('não encontrado')