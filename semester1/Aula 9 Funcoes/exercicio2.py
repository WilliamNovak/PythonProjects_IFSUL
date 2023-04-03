def square(lado):
    a = lado * lado
    p = lado * 4
    return a, p

l = float(input("Informe o lado do quadrado: "))

a, p = square(l)

print(f'O quadrado de lado {l} tem área igual a {a} e perímetro igual a {p}.')