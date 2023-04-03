s = int(input('Diga um número inteiro de 0 até 9999: '))
r = str(s)

soma  = 0
multi = 1

if s < 0 or s > 9999:
    print('Número inválido!')
else:
    print('Seus dígitos são:')
    for x in r:
        soma  += int(x)
        multi *= int(x)
        print(x)

print(f'A soma dos dígitos é {soma} e a multiplicação é {multi}.')