def testaPrimo(n):

    for x in range(2, n):
        if(n % x == 0):
            return False
    return True

n = int(input("Digite um número: "))
p = testaPrimo(n)

if(p == True):
    print(f'O número {n} é primo!')
else:
    print(f'O número {n} não é primo!')