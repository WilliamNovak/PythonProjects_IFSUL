dic = {'s': 1, 'a': 3, 'p': 1, 'i': 1, 'r': 1, 'n': 1, 'g': 1}
inverso = {}

# Loop nas chaves do dic
for chave in dic.keys():
    # Pega valor da chave no dic 
    valor = dic[chave]
    
    # Se o valor ainda não está em inverso, add valor com sua chave em sua list
    if valor not in inverso:
        inverso[valor]=[chave]
    # Se o valor já está em inverso, apenas adiciona a nova chave em sua list
    else:
        inverso[valor].append(chave)

print(inverso)
