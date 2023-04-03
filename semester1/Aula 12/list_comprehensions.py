lista1 = [2,4,6,8,10,12,14,16,18,20]

# CRIAR LISTA COM O DOBRO DOS VALORES DA LISTA 1

# Forma tradicional - loop com append
lista2 = []
for x in lista1:
    lista2.append(x*2)
print(lista2)

# Utilizando map
lista3 = list(map(lambda x: x*2,lista1))
print(lista3)

# COMPREHENSIONS
lista4 = [x*2 for x in lista1]
print(lista4)