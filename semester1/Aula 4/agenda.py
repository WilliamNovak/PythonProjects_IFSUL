agenda = {}
opcao = 1

while(opcao != 0):
    opcao = int(input('Escolha uma das opções: \n 1 - Inserir Contato \n 2 - Pesquisar Contato \n 3 - Atualizar Contato \n 4 - Mostrar Agenda \n 0 - Sair \n'))

    if(opcao not in (0,1,2,3,4)):
        print('Opção inválida!')
    else:

        if(opcao == 1):
            nome = input('Informe o nome do contato: \n')

            if(nome in agenda):
                print('Já existe um contato com esse nome!')
            else:
                telefone = input('Informe o telefone com DDD: \n')
                
                if(len(telefone) != 11):
                    print('Telefone inválido!')
                else:
                    agenda[nome] = telefone
                    print(f'Contato {nome} cadastrado!')
        
        elif(opcao == 2):
            nome = input('Informe o nome do contato para pesquisa: \n')
            print(agenda.get(nome,'Contato não encontrado.'))
        
        elif(opcao == 3):
            nome = input('Informe o nome do contato que deseja atualizar: \n')

            if nome in agenda:
                telefone = input('Informe o novo número de telefone: \n')

                if(len(telefone) != 11):
                    print('Telefone inválido!')
                else:
                    agenda[nome] = telefone
                    print(f'Contato {nome} atualizado!')
            
            else:
                print('Contato não existente!')

        elif(opcao == 4):
            print('Agenda de contatos:')

            for chave in agenda.keys():
                print(f'Contato: {chave} - Telefone: {agenda[chave]}')
