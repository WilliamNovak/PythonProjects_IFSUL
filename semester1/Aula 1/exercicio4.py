# 4 – Faça um programa em Python que receba um número inteiro e positivo e mostre se ele é primo ou não.

n1 = int(input('Informe um número inteiro e positivo: '))
primo = True

if(n1 < 0):
    print('Erro: Informe um número positivo!')
    exit()
else:
    for x in range(2, n1):
        if (n1 % x == 0):
            primo = False
            break
    
    if(primo == True):
        print(f'O número {n1} é primo!')
    else:
        print(f'O número {n1} não é primo!')
