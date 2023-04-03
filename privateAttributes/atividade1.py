class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

opcao = 1
arr = []

while opcao != 0:
    print(f'Menu:\n1 - Cadastrar\n2 - Mostrar\n0 - Sair')
    try:
        opcao = int(input('Selecione a opção que desejar ou sair: '))

        if(opcao == 1):
            nome = input('Informe o nome: ')
            try:
                idade = int(input('Informe a idade: '))
                
                if(idade > 0):
                    try:
                        cpf = int(input('Informe o cpf: '))

                        pes = Pessoa(nome, idade, cpf)

                        arr.append({'nome':pes.nome, 'idade':pes.idade, 'cpf':pes.cpf})
                        
                    except:
                        print('CPF inválido!')
                else:
                    print('Idade inválida!')
            except:
                print('Idade inválida!')

        elif(opcao == 2):
            print('Pessoas cadastradas:')
            for x in arr:
                print(f'Nome: {x["nome"]} - Idade: {x["idade"]} - CPF: {x["cpf"]}')

    except:
        print('Opção inválida!')