s = input('Diga uma string: ')
b = 0

for x in range(0,len(s)):
    if s[x] == ' ':
        b = b + 1

print(f'A string "{s}" possui {b} espaços em branco!')