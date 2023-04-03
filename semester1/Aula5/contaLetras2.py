lista=[0 ,0 ,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
s = input('Digite uma string: ')

for letra in s:
    indice = ord(letra) - 97
    print(indice)
    lista[indice] = lista[indice] + 1
    
print(lista)