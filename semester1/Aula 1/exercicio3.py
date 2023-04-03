# 3 – Faça um programa em python que receba do usuário 10 números aleatórios inteiros. Ao final do programa deve aparecer uma mensagem indicando qual maior e menor número digitado.

maior = 0
menor = 0

for x in range(1,11,1):
    n1 = int(input('Informe um número inteiro: '))

    if(x == 1):
        maior = n1
        menor = n1
    if(n1 > maior):
        maior = n1
    if(n1 < menor):
        menor = n1

print(f'O maior número informado é {maior} e o menor é {menor}!')