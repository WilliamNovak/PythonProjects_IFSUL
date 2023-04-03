import unicodedata

s = input('Digite uma frase: ')

res = unicodedata.normalize("NFD", s)
res = res.encode("ascii", "ignore")
res = res.decode("utf-8")

print(f'Frase sem acentos:\n{res}')