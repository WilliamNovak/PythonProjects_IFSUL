lista = [2,5,7,3,8,6,85,45,23,4]

# Filtra somente pelos maiores que 5
l = list(filter(lambda x:x>5, lista))
print(l)

# Pegue lista dos elementos maioires que 5 e cria uma nova lista com eles elevado ao quadrado
l2 = list(map(lambda x: x**2, l))
print(l2)

# Filtra pelas strings diferentes de ''
lista2 = ['rafael', '', 'Pablo','','felipe']
a = list(filter(lambda x:x!='', lista2))
print(a)
