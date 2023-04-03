# 5 – Faça um programa em Python que receba 2 números inteiros e positivos e mostre todos os números primos entre estes 2 números

n1 = int(input('Informe um número inteiro e positivo: '))
n2 = int(input('Informe um número inteiro e positivo: '))

if(n1 < 0 or n2 < 0):
    print('Erro: Informe somente números positivos!')
    exit()
else:
    primo = True
    print(f'Números primos entre {n1} e {n2}:')

    for x in range(n1,n2):
        for y in range(2,x):

            if(x % y == 0):
                primo =  False
        
        if(primo == True):
            print(x)
            
        primo = True