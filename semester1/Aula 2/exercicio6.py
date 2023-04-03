s = input('Diga uma string: ')
vogais = 'aeiou'
b = 0

for x in range(0,len(s)):
    if s[x] in vogais:
        b += 1

print(f'A string "{s}" possui {b} vogais!')