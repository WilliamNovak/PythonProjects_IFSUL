cadastros = {'William':99999999, 'Dionatan':123445678, 'Vini':235893467, 'Murilo': 94796794369, 'Raquel': 28357345897}

nome = input('Informe o nome do usuário: ')

print(cadastros.get(nome,'Usuário não cadastrado!'))