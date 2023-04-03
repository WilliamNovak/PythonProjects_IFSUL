c1 = {1,2,3,4,5}
c2 = {5,6,7,8,9,13}

# União de dois conjuntos
c3 = c1|c2 #c1.union(c2)

# Intersecção (Tem nos dois)
c3 = c1 & c2 # c1.intersection(c2)

# Diferença (Mostra oq tem só em c1)
c3 = c1.difference(c2)

#print(c3)

c1 = {1,2,3}
c2 = {1,2,3,4}

# Testa se c1 é um subconjunto de c2 (Todos elementos de c1 estão em c2)
print(c1 <= c2)

# Testa se c1 é subconjunto de c2, MAS c2 tem que possuir ao menos 1 elemento diferente de c1
print(c1 < c2)