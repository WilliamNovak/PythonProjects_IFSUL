#1 - Faça um programa em Python que receba um número inteiro e mostre na saída se ele é par ou impar

n1 = int(input('Informe um número inteiro: '))

resto = n1 % 2

if(resto == 0):
    print(f'O número {n1} é par!')
else:
    print(f'O número {n1} é ímpar!')