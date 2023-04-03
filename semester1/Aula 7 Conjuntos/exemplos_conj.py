# Cria conjunto (Não pode ter valores repetidos - são deletados)
c = {2,5,7,2,3,4,5,6}
# print(c)
# print(type(c))

# Remover elementos repetidos de uma LISTA --> Apenas transformar em CONJUNTO
l = [1,2,3,3,4,5,6,6,7,8,9,10,10]
c = set(l)
# print(c)

# Adicionar elementos em conjunto
c = {5,4,3,6,7,1}
c.add(10)
c.add(5)
print(c)

# Remover elemento (Remove dá erro se não acha e discard não)
# c.remove(9)
c.discard(9)

# Copia Profunda (Cópia mesmo, mesmos valores)
c1 = c.copy()
print(c1)

# Copia Rasa (Apenas interliga C2 e C1 --> Junta os valores dos dois)
c2 = c
print(c)

# Procura elemento no conjunto
if 2 in c:
    print("achou")
else:
    print("não achou")

# Conta elementos repetidos
l = [1,2,3,4,5,5,5,6,7,8,9,9,1,2,77,13]
c3 = set(l)
print(len(l) - len(c3))