s = input('Digite uma string: ')
alfa = [chr(i) for i in range(ord('a'),ord('z')+1)]

print(f'Total aparições das letras em {s}')

for x in alfa:
    count = 0

    for y in s:
        if x == y.lower():
            count = count + 1
    
    if count != 0:
        print(f'{x} : {count}')