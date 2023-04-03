s = input('Digite uma palavra: ')
n = ''

for i in range(len(s) - 1, -1, -1):
    n += s[i]

if(s.lower() == n.lower()):
    print(f'A palavra {s} é um Palindromo(Igual de trás para frente)!)')
else:
    print(f'A palavra {s} não é um Palindromo(Igual de trás para frente)!)')