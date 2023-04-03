def dividir(a,b):
    return int(a)/int(b)

try:
    n1 = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    print(f'{n1} / {n2} = {dividir(n1,n2)}')
except:
    print("Erro: Digite apenas números inteiros!")