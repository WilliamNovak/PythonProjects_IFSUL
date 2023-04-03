hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

s = input('Digite um número binário: ')
binario = 'S'

res = ''

for i in range(0, len(s)):

    if(s[i] != '0' and s[i] != '1'):
        binario = 'N'

if(binario == 'N'):

    print('Erro: Informe um número binário!')

else:
    count = 0
    num = 0
    multi = 1

    for x in range(len(s) -1, -1, -1):
        if(s[x] == '1'):
            num += multi

        # print(f'numero {s[x]} num {num} multi {multi} count{count}')

        multi *= 2
        count += 1

        if(count == 4):
            multi = 1
            count = 0

            res = hexa[num] + res
            num = 0
    
    print(f'O número Binário {s} equivale à {res} em Hexadecimal!')