def listaSobrenome(list):
    for x in list:
        newList.append(x.split())

lista=['Benjamin Walter','Charlote Freitas', 'Dionatan Jocemar','Felipe Sodré', 'Gabriel Aloisio', 'Ígor Martins','Kéllen Rocha','Lázaro Enge','Pablo Conte', 
'Pedro Henrique','Raquel Bockorny:','Stefany Sabrine','Thomas Schmidt','Vinicius Gabriel', 'Vinícius Rafael','Vitor Carvalho','William Renan','Yuri Lucas']

newList = []

listaSobrenome(lista)

newList.sort(key = lambda l: l[1])

print(newList)