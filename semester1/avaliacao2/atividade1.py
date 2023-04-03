dic  = {}

opcao = 1

while(opcao != 0):
    opcao = int(input('Escolha uma das opções: \n 1 - Cadastrar Aluno \n 2 - Inserir Notas \n 3 - Pesquisar Situação de Aluno \n 0 - Sair \n'))

    if (opcao == 1):
        nome = input('Informe o nome do aluno para cadastrar: ')

        if (nome in dic.keys()):
            print('Aluno já existente!')
        else:
            dic[nome] = {}
            print(f'Aluno {nome} cadastrado com sucesso!')

    elif (opcao == 2):
        aluno = input('Informe o nome do aluno para inserir as notas: ')

        if (aluno in dic.keys()):
            
            n1 = int(input('Informe a primeira nota: '))
            n2 = int(input('Informe a segunda nota: '))
            n3 = int(input('Informe a terceira nota: '))

            dic[aluno] = {'notas':[n1,n2,n3], 'media':[(n1+n2+n3)/3], 'situacao': ('Aprovado' if((n1+n2+n3)/3 >= 6) else 'Reprovado')}

        else:
            print('Aluno inexiste!')

    elif (opcao == 3):
        aluno = input('Informe o nome do aluno que deseja pesquisar: ')

        if (aluno in dic.keys()):
            
            if(dic[aluno] != {}):
                notas = dic[aluno]['notas']
                media = dic[aluno]['media']
                situacao = dic[aluno]['situacao']

                print(f'Aluno: {aluno} \n Notas: {notas} \n Média: {media} \n Situação: {situacao}')
            else:
                print('Aluno não possui notas cadastradas!')

        else:
            print('Aluno inexiste!')
    
    elif(opcao == 0):
        print('Programa finalizado!')

    else:
        print('Informe uma opção válida!')

print(dic)
