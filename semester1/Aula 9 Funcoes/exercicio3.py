from operator import inv


def invert(num):
    return str(num)[::-1]

num = int(input("Digite um número: "))

print(f'O número {num} ao contrário é {invert(num)}')