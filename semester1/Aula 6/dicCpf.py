from doctest import testfile


# Cria um dicionario
dic = {}

# Adiciona um cpf como chave do dicionario e outro dicionario como valor
cpf = input('Digite o cpf: \n')
dic[cpf] = {}

# Atribui uma chave nome com valor 'teste' no dicionario filho do cpf
dic[cpf]['nome'] = 'teste'

print(dic)