def testaPar(num):
    return num % 2 == 0

num = int(input("Digite um número: "))
par = testaPar(num)

if(par == True):
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é ímpar!')