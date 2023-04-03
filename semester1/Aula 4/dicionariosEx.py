#Cria um dicionário com Chaves e Valores
dic = {'banana':10, 'maçã':5, 'pão':2}

#Imprima o valor da chave
print(dic['banana'])

#Usando método Get retornando valor ou mensagem (caso não encontre)
print(dic.get('uva','Não encontrado a chave'))

#Imprime as chaves do dicionário
print(dic.keys())

#Imprime os valores do dicionário
print(dic.values())

#Imprime todo o dicionário
print(dic.items())

#Percorre dicionário com Keys
for chave in dic.keys():
    print(f'{chave}: {dic[chave]}')

#Percorre dicionário com Values
for valor in dic.values():
    print(f'{valor}')

#Percorre dicionários com items
for chave, valor in dic.items():
    print(f'{chave}: {valor}')

#Adicionar elementos ao dicionário
dic['uva'] = 20
for chave, valor in dic.items():
    print(f'{chave}: {valor}')