s = input('Digite uma String: ')
n = int(input('Digite um índice: '))

if(n <= len(s) - 1 and n >= 0 - len(s)):
    print(f'No índice {n} da string {s} há a letra {s[n]}!')
else:
    print(f'Não há o índice {n} na string {s}!')