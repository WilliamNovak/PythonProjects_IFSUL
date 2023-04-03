# Variável tipo int
# n1 = 5
# print(type(n1))

# Variável tipo string
# n1 = "palavra"
# print(type(n1))

# Input de variavel int 
#     ou string, só tirar o int
#     ou float, aceita decimais
# n1 = float(input('n1: '))
# print(type(n1))

# n2 = float(input('n1: '))
# print(type(n2))

# Soma das variaveis
# Se for dois int soma, se for duas strings concatena, tipos diferentes não aceitam soma
# s = n1 + n2

# Print concatenando com aspas e vírgulas
# print('A soma de ', n1, ' + ', n2,' é igual a ',s,'!')

# Print utilizando .format e {}
# print('O n1 vale {}, o n2 vale {} e a soma é igual a {}!'.format(n1,n2,s))

# Print com f'' --> Só funciona na versão 3.6 para cima
# :.2f formata para duas casas decimais
# print(f'A soma de {n1} + {n2} é igual a {s:.2f}!')

# Condições
# if(n1 > n2):
#     print(f'{n1} é maior que {n2}!')
# else:
#     print(f'{n2} é maior que {n1}!')

# Loop (primeiro valor, último valor, de quanto em quanto)
for x in range(0,11,2):
    print('Loop: ',x)

# Loop com break, para o código
for x in range(0,6):
    if(x == 5): break
    print('Loop: ',x)
else:
    print("Fim!")