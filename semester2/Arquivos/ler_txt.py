# Abre o arquivo e printa na tela
arq = open('teste.txt')
print(arq.read())

# Volta para o inicio do arquivo
arq.seek(0)
# Lê todo o arquivo
print(arq.read())

# Lê somente uma linha
arq.seek(0)
print(arq.readline())

# Lê linha a linha e guarda em uma lista
arq.seek(0)
lista = arq.readlines()
print(lista)