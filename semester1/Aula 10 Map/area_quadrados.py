# Imprimir area de todos quadrados
lados = [1,2,3,4,5]

# Mapeia e calcula area de cada quadrado com seu lado
quadrado = list(map (lambda x:x*x, lados))

# Mostra as áreas
print(quadrado)

# Calcula area de quadrados com lados de 1 a 10
quadradorange = list(map (lambda x:x*x, range (1,10)))
print(quadradorange)

# Se área é par mostra área, senão mostra o lado
quadradoifelse = list(map(lambda x:x*x if x%2==0 else x, range(1,20)))
print(quadradoifelse)

lados1 = [[1,2],[3,4],[5,6]]
listanova = list(map(lambda x:[x[0],x[1]*2],lados1))
print(listanova)