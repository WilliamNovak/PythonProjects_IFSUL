def testaMulti(num1, num2):
    return num2 %  num1 == 0

num1  = int(input("Informe um número: "))
num2  = int(input(f"Informe outro número para testar se é múltiplo de {num1}: "))

if(testaMulti(num1, num2) == True):
    print(f'{num2} é múltiplo de {num1}')
else:
    print(f'{num2} não é múltiplo de {num1}')