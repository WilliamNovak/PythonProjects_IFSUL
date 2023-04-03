# Cria dois dicionarios
cad1 = {'nome': 'william', 'telefone': 123456789, 'cpf': 12312312312}
cad2 = {'nome': 'Lazaro', 'telefone': 987654321, 'cpf': 98798798798}

# Cria uma lista e adiciona os dois dicionarios dentro
cadastro = []
cadastro.append(cad1)
cadastro.append(cad2)

print(cadastro)

# Loop na lista printando os dicionarios
for i in cadastro:
    print(i)

    # Loop em cada dicionario printando seus elementos
    for chave, valor in i.items():
        print(f'{chave} : {valor}')