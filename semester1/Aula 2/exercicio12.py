s = int(input('Diga um número inteiro: '))
r = str(s)

soma  = 0

for x in r:
    soma  += int(x)

print(f'A soma dos dígitos é {soma}.')