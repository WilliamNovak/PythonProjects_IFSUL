# Cria Variável String
s = "Manipulação de String"

# Printa posição 12 da variável
print(s[12])

# Printa String Inteira
print(s[:])

# Printa String das posições 0 a 11
print(s[0:11])

# Printa a String da posição 15 até o fim
print(s[15:])

# Print a String a partir da posição 0, pulando de 3 em 3
# s(INICIO:FIM:INTERVALO)
print(s[0:21:3])

# Loop para X de 0 até o tamanho da String
# for x in range(0,len(s)):
    # Imprime 1, 2, 3, 4, 5..
    # print(x)
    # Imprime a Váriavel S na posição X
    # print(s[x])

# Loop na string imprimindo posição por posição
# for x in(s):
    # print(x)

# Conta o números de caracteres A na string com Loop
c = 0
for x in s:
    if(x == 'a'):
        c = c + 1
print(c)

# Contar caracteres com função count
C = s.count('a')
print(C)

# Função Find retorna o índice da PRIMEIRA ocorrência em que a String informada é encontrada
C = s.find('a')
print(C)

# Loop para mostrar todos os índices de ocorrência de uma string em outra
indice = 0

while indice < len(s):
    # if(s[indice] == 'a'):
        # print(indice)
    indice = indice + 1