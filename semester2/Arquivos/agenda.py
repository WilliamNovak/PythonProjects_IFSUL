achou = 0

while True:
    opcao = int(input('Escolha uma opção (1 - Cadastrar, 2 - Consultar, 3 - Sair): '))

    if (opcao == 1):
        nome = input('Digite o nome do contato: ')
        num  = int(input('Digite o telefone: '))

        with open('agenda.txt','r') as agenda:
            contatos = agenda.readlines()
            linhas = len(contatos)

            agenda.seek(0)
            for linha in range(0, linhas):
                contato = agenda.readline().replace('\n','')

                if (contato == nome):
                    achou = 1
            
            if (achou == 0):
                with open('agenda.txt','a') as agenda:
                    agenda.write(f"{nome}\n")
                    agenda.write(f"{num}\n")
            else:
                print(f'Já existe um contato com o nome {nome}')
                achou = 0

    elif (opcao == 2):
        nome = input('Digite o nome do contato: ')

        with open('agenda.txt','r') as agenda:
            contatos = agenda.readlines()
            linhas = len(contatos)

            agenda.seek(0)
            for linha in range(0, linhas):
                contato = agenda.readline().replace('\n','')

                if (contato == nome):
                    numero = agenda.readline()
                    print(f'Contato: {nome} - Número: {numero}')
                    achou = 1
            
            if (achou == 0):
                print('Contato inexistente!')
            
            achou = 0

    elif (opcao == 3):
        print('Agenda finalizada.')
        break
    
    else:
        print('Opção inválida!')