b = int(input('Digite um número binário: '))
s = str(b)
binario = 'S'

multi = 1
res = 0

for i in range(0, len(s)):

    if(s[i] != '0' and s[i] != '1'):
        binario = 'N'

if(binario == 'N'):

    print('Erro: Informe um número binário!')

else:
    for x in range(len(s) - 1, -1, -1):
        
        if(s[x] == '1'):
            res += multi
        
        multi *= 2

    print(f'O número {b} equivale à {res} em decimal!')