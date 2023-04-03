import imp
import unicodedata
import string

res = ''

s = input('Digite uma frase: ')
r = s.replace(' ','')

a = unicodedata.normalize("NFD", r)
a = a.encode("ascii", "ignore")
a = a.decode("utf-8")

new_string = a.translate(str.maketrans('', '', string.punctuation))

for i in range(len(new_string) - 1, -1, -1):
    res += new_string[i]

if(new_string.lower() == res.lower()):
    print(f'A frase "{s}" é um Palindromo(Igual de trás para frente)!)')
else:
    print(f'A frase "{s}" não é um Palindromo(Igual de trás para frente)!)')